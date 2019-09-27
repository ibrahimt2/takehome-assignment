<template>
  <!-- PART 4: Add your code here -->
  <div>
    <p>{{name}}</p>
    <Counter v-bind:count='episodes_seen'></Counter>
  </div>
</template>

<script>

export default {
  
  props:[]

}
</script>

<style>
</style>
