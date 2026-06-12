"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWebLink``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_web_link_device_type
    import aws_sdk_geo_routes.types.sensitive_string


class RouteWebLink(TypedDict):
    anchor_text: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>The interactive or clickable portion of the text.</p>"""
    description: "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Text describing the URL.</p>"""
    device_type: NotRequired[
        "aws_sdk_geo_routes.types.route_web_link_device_type.RouteWebLinkDeviceType"
    ]
    """<p>Device type for which the link is intended.</p>"""
    url: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The URL of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteWebLink) -> dict:
    out: dict = {}
    if "anchor_text" in value:
        out["AnchorText"] = value["anchor_text"]
    out["Description"] = value["description"]
    if "device_type" in value:
        import aws_sdk_geo_routes.types.route_web_link_device_type

        out["DeviceType"] = (
            aws_sdk_geo_routes.types.route_web_link_device_type.serialize_json(
                value["device_type"]
            )
        )
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RouteWebLink:
    out: RouteWebLink = {}  # type: ignore[typeddict-item]
    if "AnchorText" in data:
        out["anchor_text"] = data["AnchorText"]
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("RouteWebLink.description required")
    if "DeviceType" in data:
        import aws_sdk_geo_routes.types.route_web_link_device_type

        out["device_type"] = (
            aws_sdk_geo_routes.types.route_web_link_device_type.deserialize_json(
                data["DeviceType"]
            )
        )
    if "Url" in data:
        out["url"] = data["Url"]
    return out
