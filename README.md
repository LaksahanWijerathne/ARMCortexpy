# ARMCortexpy 🐍⚙️

**Pythonic syntax meets ARM Cortex performance**  
*A transpiler that converts Python-like code to optimized STM32 HAL/C, making embedded development faster and more accessible.*

```python
# Example (blink.acpy)
import armcortexpy.stm32 as stm
led = stm.GPIO('PA5', stm.OUT)
while True:
    led.toggle()
    stm.delay(500.ms)  # → HAL_Delay(500)

