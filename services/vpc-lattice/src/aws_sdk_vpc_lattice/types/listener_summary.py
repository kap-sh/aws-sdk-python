"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListenerSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.listener_arn
    import aws_sdk_vpc_lattice.types.listener_id
    import aws_sdk_vpc_lattice.types.listener_name
    import aws_sdk_vpc_lattice.types.listener_protocol
    import aws_sdk_vpc_lattice.types.port
    import aws_sdk_vpc_lattice.types.timestamp


class ListenerSummary(TypedDict):
    arn: NotRequired["aws_sdk_vpc_lattice.types.listener_arn.ListenerArn"]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    id: NotRequired["aws_sdk_vpc_lattice.types.listener_id.ListenerId"]
    """<p>The ID of the listener.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.listener_name.ListenerName"]
    """<p>The name of the listener.</p>"""
    protocol: NotRequired[
        "aws_sdk_vpc_lattice.types.listener_protocol.ListenerProtocol"
    ]
    """<p>The listener protocol.</p>"""
    port: NotRequired["aws_sdk_vpc_lattice.types.port.Port"]
    """<p>The listener port.</p>"""
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the listener was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "port" in value:
        out["port"] = value["port"]
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ListenerSummary:
    out: ListenerSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "port" in data:
        out["port"] = data["port"]
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
