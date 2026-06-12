"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryStatusMonitorTopContributorsInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.resource_name

class GetQueryStatusMonitorTopContributorsInput(TypedDict):
    monitor_name: "aws_sdk_networkflowmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatusMonitorTopContributorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryStatusMonitorTopContributorsInput:
    out: GetQueryStatusMonitorTopContributorsInput = {}  # type: ignore[typeddict-item]
    return out