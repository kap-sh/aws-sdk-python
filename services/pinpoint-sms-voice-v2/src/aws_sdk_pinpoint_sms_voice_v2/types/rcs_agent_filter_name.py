"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsAgentFilterName``."""

from typing import TypeAlias

"""<p>The filter name for filtering RCS agents. The available filter names are:</p> <ul> <li> <p> <code>deletion-protection-enabled</code>: Filter by deletion protection status.</p> </li> <li> <p> <code>opt-out-list-name</code>: Filter by the opt-out list name.</p> </li> <li> <p> <code>self-managed-opt-outs-enabled</code>: Filter by self-managed opt-outs status.</p> </li> <li> <p> <code>status</code>: Filter by RCS agent status.</p> </li> <li> <p> <code>two-way-channel-arn</code>: Filter by the two-way channel ARN.</p> </li> <li> <p> <code>two-way-enabled</code>: Filter by two-way enabled status.</p> </li> </ul>"""
RcsAgentFilterName: TypeAlias = str
