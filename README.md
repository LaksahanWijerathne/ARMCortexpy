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
```

## Key Features ✨

* Python-like syntax with strict typing for reliability

* Direct STM32 HAL mapping – no hidden overhead

* Batteries-included peripherals (GPIO, UART, I2C, etc.)

* STM32CubeMX integration – sync your .ioc configs

* Compiles to clean C with LLVM optimization support

# Quick Start 🚀

## Installation
```python
pip install arm-cortexpy  # Python package
armcortexpy install-tools  # ARM GCC, OpenOCD
```

## Your First Project
1. Create blink.acpy (see example above)
2. Generate STM32CubeMX project
3. Compile & flash:

```python
armcortexpy build blink.acpy --target stm32f411 --flash
```

## Hardware Support 🎛️

**Board**

* STM32F4xx : Full HAL support

* STM32H7xx : Beta (no cache opts)

* Raspberry Pi Pico :   Coming soon!

## Documentation 📚

**Language Syntax**
* STM32 HAL Mapping
* Debugging Tips

## Contributing
We welcome PRs! for:

* Adding new MCU families
* Improving error messages
* Creating more examples


