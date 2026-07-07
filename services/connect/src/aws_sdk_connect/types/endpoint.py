"""Generated from Smithy shape ``com.amazonaws.connect#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.endpoint_address
    import aws_sdk_connect.types.endpoint_type


class Endpoint(TypedDict, closed=True):
    type: NotRequired["aws_sdk_connect.types.endpoint_type.EndpointType"]
    """<p>Type of the endpoint.</p>"""
    address: NotRequired["aws_sdk_connect.types.endpoint_address.EndpointAddress"]
    """<p>Address of the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Endpoint) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_connect.types.endpoint_type

        out["Type"] = aws_sdk_connect.types.endpoint_type.serialize_json(value["type"])
    if "address" in value:
        out["Address"] = value["address"]
    return out


def deserialize_json(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connect.types.endpoint_type

        out["type"] = aws_sdk_connect.types.endpoint_type.deserialize_json(data["Type"])
    if "Address" in data:
        out["address"] = data["Address"]
    return out
