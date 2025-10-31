from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import strawberry
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class User:
    id: int
    name: str
    age: int


database: list[User] = [
    User(
        id=1,
        name="Коля",
        age=20,
    ),
    User(
        id=2,
        name="Влад",
        age=20,
    ),
]


@strawberry.type
class Query:
    @strawberry.field
    def get_user(
        id: int,
    ) -> User:
        for elem in database:
            if elem.id == id:
                return elem
        return User(
            id=-1,
            name="No name",
            age=666,
        )

    @strawberry.field
    def get_users() -> list[User]:
        return database


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(
        id: int,
        name: str,
        age: int,
    ) -> User:
        new_user = User(
            id=id,
            name=name,
            age=age,
        )
        database.append(new_user)
        return new_user

    @strawberry.mutation
    def delete_user(
        id: int,
    ) -> None:
        for i in range(len(database)):
            if database[i].id == id:
                database.pop(i)
                break

    @strawberry.mutation
    def update_user(
        id: int,
        name: str,
        age: int,
    ) -> User:
        for elem in database:
            if elem.id == id:
                elem.name = name
                elem.age = age
                return elem


schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
graphql_app = GraphQLRouter(schema=schema)
app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    uvicorn.run(app)
