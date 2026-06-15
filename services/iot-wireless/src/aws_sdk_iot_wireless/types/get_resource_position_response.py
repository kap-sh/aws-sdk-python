"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetResourcePositionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.geo_json_payload


class GetResourcePositionResponse(TypedDict):
    geo_json_payload: NotRequired[
        "aws_sdk_iot_wireless.types.geo_json_payload.GeoJsonPayload"
    ]
    r"""<p>The position information of the resource, displayed as a JSON payload. The payload uses the GeoJSON format, which a format that's used to encode geographic data structures. For more information, see <a href=\"https://geojson.org/\">GeoJSON</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePositionResponse) -> dict:
    out: dict = {}
    if "geo_json_payload" in value:
        import aws_sdk_iot_wireless.types.geo_json_payload

        out["GeoJsonPayload"] = (
            aws_sdk_iot_wireless.types.geo_json_payload.serialize_json(
                value["geo_json_payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetResourcePositionResponse:
    out: GetResourcePositionResponse = {}  # type: ignore[typeddict-item]
    if "GeoJsonPayload" in data:
        import aws_sdk_iot_wireless.types.geo_json_payload

        out["geo_json_payload"] = (
            aws_sdk_iot_wireless.types.geo_json_payload.deserialize_json(
                data["GeoJsonPayload"]
            )
        )
    return out
