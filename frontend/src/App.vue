<script setup>
import { useQuery } from '@vue/apollo-composable'
import { computed } from 'vue'
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

const users = computed(() => result.value?.getUsers || [])
</script>

<template>
  <h1>You did it!</h1>
  <div v-if="error" class="error">{{ error.message }}</div>
  <div v-else-if="loading" class="loading">Loading...</div>
  <div v-else>
    <table border="1">
      <tr>
        <td>ID</td>
        <td>NAME</td>
        <td>AGE</td>
      </tr>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.age }}</td>
      </tr>
    </table>
  </div>
</template>

<style scoped>
td {
  padding: 10px;
}
</style>