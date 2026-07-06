"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetAssetPropertyValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_value


class GetAssetPropertyValueResponse(TypedDict, closed=True):
    property_value: NotRequired[
        "aws_sdk_iotsitewise.types.asset_property_value.AssetPropertyValue"
    ]
    """<p>The current asset property value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetPropertyValueResponse) -> dict:
    out: dict = {}
    if "property_value" in value:
        import aws_sdk_iotsitewise.types.asset_property_value

        out["propertyValue"] = (
            aws_sdk_iotsitewise.types.asset_property_value.serialize_json(
                value["property_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssetPropertyValueResponse:
    out: GetAssetPropertyValueResponse = {}  # type: ignore[typeddict-item]
    if "propertyValue" in data:
        import aws_sdk_iotsitewise.types.asset_property_value

        out["property_value"] = (
            aws_sdk_iotsitewise.types.asset_property_value.deserialize_json(
                data["propertyValue"]
            )
        )
    return out
