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

     **Security note**: Updates to ProcessMaker may require supervision so
     they **ARE NOT** configured to install automatically. See `ProcessMaker
     documentation`_ for upgrading (please note link is to 3.2 upgrade - 
     please adjust as per version you are upgrading to).

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
   12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Adminer: username **adminer**
-  ProcessMaker: username **admin**


.. _ProcessMaker: http://www.processmaker.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _ProcessMaker documentation: https://wiki.processmaker.com/3.2/Upgrading_ProcessMaker
.. _Adminer: http://www.adminer.org/
