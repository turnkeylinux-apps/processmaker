ProcessMaker - Workflow & BPM software
======================================

`ProcessMaker`_ helps business analysts improve workflow performance by
discovering and analyzing process inefficiencies and bottlenecks.
Automated notifications and an intuitive drag-and-drop web interface
allow users to easily interact with your form-driven processes. Managers
receive KPIs and metrics from reports and dashboards.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- ProcessMaker configurations:
   
   - Installed from upstream source code to /var/www/processmaker

- SSL support out of the box.
- `PHPMyAdmin`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, phpMyAdmin: username **root**
-  ProcessMaker: username **admin**


.. _ProcessMaker: http://www.processmaker.com/
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _PHPMyAdmin: http://www.phpmyadmin.net
