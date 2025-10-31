<script setup>
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'

const GET_USERS = gql`
  query GetUsers {
    getUsers {
      id
      name
      age
    }
  }
`

const { result, loading, error } = useQuery(GET_USERS)
</script>

<template>
  <h1>You did it!</h1>
  <h2>{{ result }}</h2>
  <h2>{{ loading }}</h2>
  <h2>{{ error }}</h2>
</template>
