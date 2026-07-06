"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetQueryStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.resource_name


class GetQueryStatusInput(TypedDict, closed=True):
    monitor_name: "aws_sdk_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    query_id: "str"
    """<p>The ID of the query that you want to return the status for. A <code>QueryId</code> is an internally-generated dentifier for a specific query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueryStatusInput:
    out: GetQueryStatusInput = {}  # type: ignore[typeddict-item]
    return out
