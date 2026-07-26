"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TierUpgradeStatus``."""

from typing import TypeAlias

"""<p>The tier upgrade status of a notify configuration.</p> <ul> <li> <p> <code>BASIC</code> - Currently at basic tier.</p> </li> <li> <p> <code>PENDING_UPGRADE</code> - Upgrade to advanced tier is pending.</p> </li> <li> <p> <code>ADVANCED</code> - Currently at advanced tier.</p> </li> <li> <p> <code>REJECTED</code> - Tier upgrade was rejected.</p> </li> </ul>"""
TierUpgradeStatus: TypeAlias = str
