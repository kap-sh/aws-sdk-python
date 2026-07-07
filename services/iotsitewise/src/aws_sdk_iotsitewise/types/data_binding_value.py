"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataBindingValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property_binding_value
    import aws_sdk_iotsitewise.types.asset_property_binding_value


class DataBindingValue(TypedDict, closed=True):
    asset_model_property: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_property_binding_value.AssetModelPropertyBindingValue"
    ]
    asset_property: NotRequired[
        "aws_sdk_iotsitewise.types.asset_property_binding_value.AssetPropertyBindingValue"
    ]
    """<p>The asset property value used in the data binding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataBindingValue) -> dict:
    out: dict = {}
    if "asset_model_property" in value:
        import aws_sdk_iotsitewise.types.asset_model_property_binding_value

        out["assetModelProperty"] = (
            aws_sdk_iotsitewise.types.asset_model_property_binding_value.serialize_json(
                value["asset_model_property"]
            )
        )
    if "asset_property" in value:
        import aws_sdk_iotsitewise.types.asset_property_binding_value

        out["assetProperty"] = (
            aws_sdk_iotsitewise.types.asset_property_binding_value.serialize_json(
                value["asset_property"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataBindingValue:
    out: DataBindingValue = {}  # type: ignore[typeddict-item]
    if "assetModelProperty" in data:
        import aws_sdk_iotsitewise.types.asset_model_property_binding_value

        out["asset_model_property"] = (
            aws_sdk_iotsitewise.types.asset_model_property_binding_value.deserialize_json(
                data["assetModelProperty"]
            )
        )
    if "assetProperty" in data:
        import aws_sdk_iotsitewise.types.asset_property_binding_value

        out["asset_property"] = (
            aws_sdk_iotsitewise.types.asset_property_binding_value.deserialize_json(
                data["assetProperty"]
            )
        )
    return out
