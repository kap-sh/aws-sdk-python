"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectionHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connection_status
    import aws_sdk_networkmanager.types.connection_type
    import aws_sdk_networkmanager.types.date_time


class ConnectionHealth(TypedDict, closed=True):
    type: NotRequired["aws_sdk_networkmanager.types.connection_type.ConnectionType"]
    """<p>The connection type.</p>"""
    status: NotRequired[
        "aws_sdk_networkmanager.types.connection_status.ConnectionStatus"
    ]
    """<p>The connection status.</p>"""
    timestamp: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The time the status was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionHealth) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_networkmanager.types.connection_type

        out["Type"] = aws_sdk_networkmanager.types.connection_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_networkmanager.types.connection_status

        out["Status"] = aws_sdk_networkmanager.types.connection_status.serialize_json(
            value["status"]
        )
    if "timestamp" in value:
        import aws_sdk_networkmanager.types.date_time

        out["Timestamp"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ConnectionHealth:
    out: ConnectionHealth = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_networkmanager.types.connection_type

        out["type"] = aws_sdk_networkmanager.types.connection_type.deserialize_json(
            data["Type"]
        )
    if "Status" in data:
        import aws_sdk_networkmanager.types.connection_status

        out["status"] = aws_sdk_networkmanager.types.connection_status.deserialize_json(
            data["Status"]
        )
    if "Timestamp" in data:
        import aws_sdk_networkmanager.types.date_time

        out["timestamp"] = aws_sdk_networkmanager.types.date_time.deserialize_json(
            data["Timestamp"]
        )
    return out
