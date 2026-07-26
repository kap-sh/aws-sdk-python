"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ConnectionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.connection_status
    import capo_iotsecuretunneling.types.date_type


class ConnectionState(TypedDict, closed=True):
    status: NotRequired[
        "capo_iotsecuretunneling.types.connection_status.ConnectionStatus"
    ]
    """<p>The connection status of the tunnel. Valid values are <code>CONNECTED</code> and <code>DISCONNECTED</code>.</p>"""
    last_updated_at: NotRequired["capo_iotsecuretunneling.types.date_type.DateType"]
    """<p>The last time the connection status was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionState) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_iotsecuretunneling.types.connection_status

        out["status"] = (
            capo_iotsecuretunneling.types.connection_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_updated_at" in value:
        import capo_iotsecuretunneling.types.date_type

        out["lastUpdatedAt"] = (
            capo_iotsecuretunneling.types.date_type.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionState:
    out: ConnectionState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_iotsecuretunneling.types.connection_status

        out["status"] = (
            capo_iotsecuretunneling.types.connection_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "lastUpdatedAt" in data:
        import capo_iotsecuretunneling.types.date_type

        out["last_updated_at"] = (
            capo_iotsecuretunneling.types.date_type.deserialize_aws_json_1_1(
                data["lastUpdatedAt"]
            )
        )
    return out
