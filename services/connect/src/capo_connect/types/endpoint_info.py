"""Generated from Smithy shape ``com.amazonaws.connect#EndpointInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.endpoint_address
    import capo_connect.types.endpoint_display_name
    import capo_connect.types.endpoint_type


class EndpointInfo(TypedDict, closed=True):
    type: NotRequired["capo_connect.types.endpoint_type.EndpointType"]
    """<p>Type of endpoint.</p>"""
    address: NotRequired["capo_connect.types.endpoint_address.EndpointAddress"]
    """<p>Address of the endpoint.</p>"""
    display_name: NotRequired[
        "capo_connect.types.endpoint_display_name.EndpointDisplayName"
    ]
    """<p>Display name of the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointInfo) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_connect.types.endpoint_type

        out["Type"] = capo_connect.types.endpoint_type.serialize_json(value["type"])
    if "address" in value:
        out["Address"] = value["address"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> EndpointInfo:
    out: EndpointInfo = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_connect.types.endpoint_type

        out["type"] = capo_connect.types.endpoint_type.deserialize_json(data["Type"])
    if "Address" in data:
        out["address"] = data["Address"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    return out
