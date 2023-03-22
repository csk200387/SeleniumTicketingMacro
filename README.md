# SeleniumTicketingMacro
셀레니움 티켓팅 매크로 예제

# 1. find_element()
어느 순간부터 바뀌었는지 
`find_element_by_****(arg)` 메서드가 `find_element(By.****, arg)` 로 바뀌었다. 아래와 같이 By를 import 하여 사용해야 한다.
```python
from selenium.webdriver.common.by import By
```

# 2. implicitly_wait()
일반적인 time.sleep() 보다 더 나은 효율을 보일 수 있다. 다음 Element를 찾을 때 까지 기다린다.
아래는 Selenium Docs의 발췌 내용
> An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0 (zero). Once set, the implicit wait is set for the life of the WebDriver object.

> 암시적 대기는 즉시 사용할 수 없는 요소를 찾으려고 할 때 웹 드라이버가 일정 시간 동안 DOM을 폴링하도록 지시합니다. 기본 설정은 0(0)입니다. 설정되면 암시적 대기는 WebDriver 객체의 수명 동안 설정됩니다.


# 3. .switch_to.frame()
예매창의 페이지 소스를 확인하여 iframe 태그가 존재하는지 확인해야 한다. frame 전환을 하지 않을 경우 Element를 찾지 못한다.
