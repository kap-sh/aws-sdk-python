"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListMonitorsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.max_results
    import aws_sdk_networkflowmonitor.types.monitor_status

class ListMonitorsInput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["aws_sdk_networkflowmonitor.types.max_results.MaxResults"]
    """<p>The number of query results that you want to return with this call.</p>"""
    monitor_status: NotRequired["aws_sdk_networkflowmonitor.types.monitor_status.MonitorStatus"]
    """<p>The status of a monitor. The status can be one of the following</p> <ul> <li> <p> <code>PENDING</code>: The monitor is in the process of being created.</p> </li> <li> <p> <code>ACTIVE</code>: The monitor is active.</p> </li> <li> <p> <code>INACTIVE</code>: The monitor is inactive.</p> </li> <li> <p> <code>ERROR</code>: Monitor creation failed due to an error.</p> </li> <li> <p> <code>DELETING</code>: The monitor is in the process of being deleted.</p> </li> </ul>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMonitorsInput:
    out: ListMonitorsInput = {}  # type: ignore[typeddict-item]
    return out