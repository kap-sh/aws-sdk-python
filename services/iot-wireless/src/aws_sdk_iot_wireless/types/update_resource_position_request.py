"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateResourcePositionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.geo_json_payload
    import aws_sdk_iot_wireless.types.position_resource_identifier
    import aws_sdk_iot_wireless.types.position_resource_type


class UpdateResourcePositionRequest(TypedDict):
    resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    """<p>The identifier of the resource for which position information is updated. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.</p>"""
    resource_type: (
        "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType"
    )
    """<p>The type of resource for which position information is updated, which can be a wireless device or a wireless gateway.</p>"""
    geo_json_payload: NotRequired[
        "aws_sdk_iot_wireless.types.geo_json_payload.GeoJsonPayload"
    ]
    """<p>The position information of the resource, displayed as a JSON payload. The payload uses the GeoJSON format, which a format that's used to encode geographic data structures. For more information, see <a href=\"https://geojson.org/\">GeoJSON</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourcePositionRequest) -> dict:
    out: dict = {}
    if "geo_json_payload" in value:
        import aws_sdk_iot_wireless.types.geo_json_payload

        out["GeoJsonPayload"] = (
            aws_sdk_iot_wireless.types.geo_json_payload.serialize_json(
                value["geo_json_payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResourcePositionRequest:
    out: UpdateResourcePositionRequest = {}  # type: ignore[typeddict-item]
    if "GeoJsonPayload" in data:
        import aws_sdk_iot_wireless.types.geo_json_payload

        out["geo_json_payload"] = (
            aws_sdk_iot_wireless.types.geo_json_payload.deserialize_json(
                data["GeoJsonPayload"]
            )
        )
    return out
