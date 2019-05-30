# Custom Robot Framework Metrics Report

Similar as [robotframework-metric](https://github.com/adiralashiva8/robotframework-metrics) project but keywords stats are not included in this project

[![HitCount](http://hits.dwyl.io/adiralashiva8/robotframework-metrics-custom.svg)](http://hits.dwyl.io/adiralashiva8/robotframework-metrics-custom)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

---

#### How it Works:

1. Read output.xml file using robotframework API
2. Get Suite, Test Case Status and Elapsed time values
3. Convert data to html report using Beautifulsoup

---

#### How to use in project:

1. Install robotmetrics 

    > Using setup.py (clone project and run command within root)
    ```
    python setup.py install
    ```

2. Execute robotcmetrics command to generate report

    > Case 1: No change in output.xml, log.html file name's and user is in same folder
    ```
    robotcmetrics
    ```
    > Case 2: Change in output.xml, log.html file name's And .xml and .html files are under 'Result' folder
    ```
    robotcmetrics --inputpath ./Result/ --output "output1.xml" --log "log1.html"
    ```
    robotframework-metrics can parse multiple xmls at a time. Following is the command
    ```
    robotcmetrics --inputpath ./Result/ --output "output1.xml,output2.xml" --log "log1.html"
    ```
    
    > For more info on command line options use:

    ```
    robotcmetrics --help
    ```
    
3. RobotFramework Metrics Report __metric-timestamp.html__ file will be created in current folder | `-inputpath` if specified

---

#### Customize Report

Specify Logo in Robotframework metrics: 

 - __Custom Logo__ : Customize your logo by using --logo command line option

     ```
     --logo "https://mycompany/logo.jpg"
     ```
---

#### Generate robotframework-metrics after execution

Execute robotmetrics command after suite or test execution as follows:

 - Create .bat (or) .sh file with following snippet

    ```
    robot test.robot &&
    robotcmetrics [:options]
    ```

    > && is used to execute multiple command's in .bat file

  - Modify robotmetrics command as required and execute .bat file
  
  - Robotframework metrics will be created after execution

---

If you have any questions / suggestions / comments on the report, please feel free to reach me at

 - Email: <a href="mailto:adiralashiva8@gmail.com?Subject=Robotframework%20Metrics" target="_blank">`adiralashiva8@gmail.com`</a> 
 - Slack: <a href="https://robotframework.slack.com/messages/robotframeworkmetrics" target="_blank">`robotframeworkmetrics`</a>
 - LinkedIn: <a href="https://www.linkedin.com/in/shivaprasadadirala/" target="_blank">`shivaprasadadirala`</a>
 - Twitter: <a href="https://twitter.com/ShivaAdirala" target="_blank">`@ShivaAdirala`</a>

---