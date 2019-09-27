<template>
  <!-- PART 4: Add your code here -->
  <div>
    <p>{{name}}</p>
    <Counter v-bind:count='episodes_seen'></Counter>
  </div>
</template>

<script>
import Counter from "./Counter.vue";

export default {
  
  components: {
    Counter
  },
  
  props: {
    name: {
      type: String
    },
    episodes_seen: {
      type: Number
    },
    id: {
      type: Number
    }
  }

}
</script>

<style>
</style>
