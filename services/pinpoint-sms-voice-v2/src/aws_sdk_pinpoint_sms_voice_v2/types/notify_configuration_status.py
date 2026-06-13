"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyConfigurationStatus``."""

from typing import TypeAlias

"""<p>The status of a notify configuration.</p> <ul> <li> <p> <code>PENDING</code> - The notify configuration is pending review.</p> </li> <li> <p> <code>ACTIVE</code> - The notify configuration is active and can be used.</p> </li> <li> <p> <code>REJECTED</code> - The notify configuration was rejected.</p> </li> <li> <p> <code>REQUIRES_VERIFICATION</code> - The notify configuration requires verification.</p> </li> </ul>"""
NotifyConfigurationStatus: TypeAlias = str
