"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.integer
    import aws_sdk_migrationhubstrategy.types.server_os_type


class ServerSummary(TypedDict, closed=True):
    server_os_type: NotRequired[
        "aws_sdk_migrationhubstrategy.types.server_os_type.ServerOsType"
    ]
    """<p> Type of operating system for the servers. </p>"""
    count: NotRequired["aws_sdk_migrationhubstrategy.types.integer.Integer"]
    """<p> Number of servers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSummary) -> dict:
    out: dict = {}
    if "server_os_type" in value:
        out["ServerOsType"] = value["server_os_type"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> ServerSummary:
    out: ServerSummary = {}  # type: ignore[typeddict-item]
    if "ServerOsType" in data:
        out["server_os_type"] = data["ServerOsType"]
    if "count" in data:
        out["count"] = data["count"]
    return out
