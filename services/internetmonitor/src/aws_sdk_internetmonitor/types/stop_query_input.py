"""Generated from Smithy shape ``com.amazonaws.internetmonitor#StopQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.resource_name


class StopQueryInput(TypedDict, closed=True):
    monitor_name: "aws_sdk_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    query_id: "str"
    """<p>The ID of the query that you want to stop. A <code>QueryId</code> is an internally-generated identifier for a specific query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopQueryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopQueryInput:
    out: StopQueryInput = {}  # type: ignore[typeddict-item]
    return out
