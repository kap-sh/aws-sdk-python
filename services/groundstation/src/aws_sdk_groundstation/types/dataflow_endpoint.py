"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.endpoint_status
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.socket_address


class DataflowEndpoint(TypedDict):
    name: NotRequired["aws_sdk_groundstation.types.safe_name.SafeName"]
    """<p>Name of a dataflow endpoint.</p>"""
    address: NotRequired["aws_sdk_groundstation.types.socket_address.SocketAddress"]
    """<p>Socket address of a dataflow endpoint.</p>"""
    status: NotRequired["aws_sdk_groundstation.types.endpoint_status.EndpointStatus"]
    """<p>Status of a dataflow endpoint.</p>"""
    mtu: NotRequired["int"]
    """<p>Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEndpoint) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "address" in value:
        import aws_sdk_groundstation.types.socket_address

        out["address"] = aws_sdk_groundstation.types.socket_address.serialize_json(
            value["address"]
        )
    if "status" in value:
        import aws_sdk_groundstation.types.endpoint_status

        out["status"] = aws_sdk_groundstation.types.endpoint_status.serialize_json(
            value["status"]
        )
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    return out


def deserialize_json(data: dict) -> DataflowEndpoint:
    out: DataflowEndpoint = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "address" in data:
        import aws_sdk_groundstation.types.socket_address

        out["address"] = aws_sdk_groundstation.types.socket_address.deserialize_json(
            data["address"]
        )
    if "status" in data:
        import aws_sdk_groundstation.types.endpoint_status

        out["status"] = aws_sdk_groundstation.types.endpoint_status.deserialize_json(
            data["status"]
        )
    if "mtu" in data:
        out["mtu"] = data["mtu"]
    return out
