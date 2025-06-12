# PyMCUcore 🐍⚙️

**Pythonic syntax meets C/C++ performance**  
*A transpiler that converts Python-like code to optimized HAL/C, making embedded development faster and more accessible.*

```python
# Example (blink.acpy)
import pymcu.stm32 as stm
led = stm.GPIO('PA5', stm.OUT)
while True:
    led.toggle()
    stm.delay(500.ms)  # → HAL_Delay(500)
```

## Key Features ✨

* Python-like syntax with strict typing for reliability

* Direct HAL mapping – no hidden overhead

* Batteries-included peripherals (GPIO, UART, I2C, etc.)

* STM32CubeMX / MCU_SDK integration – sync your configs

* Compiles to clean C with LLVM optimization support

# Quick Start 🚀

## Installation
```python
pip install pymcucore  # Python package
pymcucore install-tools  # ARM GCC, OpenOCD
```

## Your First Project
1. Create blink.acpy (see example above)
2. Generate STM32CubeMX project
3. Compile & flash:

```python
pymcucore build blink.acpy --target stm32f411 --flash
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

## Community 💬

Join us on:

* Discord(https://discord.gg/JhS6u3Yt)

