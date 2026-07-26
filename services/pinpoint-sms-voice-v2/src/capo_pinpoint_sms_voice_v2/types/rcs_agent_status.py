"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsAgentStatus``."""

from typing import TypeAlias

"""<p>The current status of the RCS agent.</p> <ul> <li> <p> <code>CREATED</code>: The RCS agent has been created.</p> </li> <li> <p> <code>PENDING</code>: The RCS agent is pending review.</p> </li> <li> <p> <code>TESTING</code>: The RCS agent is in testing.</p> </li> <li> <p> <code>PARTIAL</code>: The RCS agent is partially active.</p> </li> <li> <p> <code>ACTIVE</code>: The RCS agent is active and available for use.</p> </li> <li> <p> <code>DELETED</code>: The RCS agent has been deleted.</p> </li> </ul>"""
RcsAgentStatus: TypeAlias = str
