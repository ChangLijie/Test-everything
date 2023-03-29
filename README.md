# Multi thread Test.
When we use multi thread with light-load. It will run in the same core.  
![This is a alt text.](./docs/threadpool_light-load.gif "This is a sample image.")  
When we use multi thread with power-load. It will run in the different core.  
![This is a alt text.](./docs/threadpool_power-load.gif "This is a sample image.")  

# Multi process Test.
When we run multi process , memory might be overload!
![This is a alt text.](./docs/multiprocess.gif "This is a sample image.")

# Difference between multi thread and multi process.

|               | Multi thread              | Multi process                         |
| ------------- |:-------------------------:|:-------------------------------------:|
| Memory        | share the same memory.    |Every process has is own memory space. |
| apply to      | IO-bound task.            |CPU-bound task.                        |

