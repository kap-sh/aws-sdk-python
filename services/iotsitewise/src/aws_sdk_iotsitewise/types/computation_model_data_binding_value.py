"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelDataBindingValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property_binding_value
    import aws_sdk_iotsitewise.types.asset_property_binding_value
    import aws_sdk_iotsitewise.types.binding_value_list


class ComputationModelDataBindingValue(TypedDict):
    asset_model_property: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_property_binding_value.AssetModelPropertyBindingValue"
    ]
    """<p>Specifies an asset model property data binding value.</p>"""
    asset_property: NotRequired[
        "aws_sdk_iotsitewise.types.asset_property_binding_value.AssetPropertyBindingValue"
    ]
    """<p>The asset property value used for computation model data binding.</p>"""
    list: NotRequired["aws_sdk_iotsitewise.types.binding_value_list.BindingValueList"]
    """<p>Specifies a list of data binding value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelDataBindingValue) -> dict:
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
    if "list" in value:
        import aws_sdk_iotsitewise.types.binding_value_list

        out["list"] = aws_sdk_iotsitewise.types.binding_value_list.serialize_json(
            value["list"]
        )
    return out


def deserialize_json(data: dict) -> ComputationModelDataBindingValue:
    out: ComputationModelDataBindingValue = {}  # type: ignore[typeddict-item]
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
    if "list" in data:
        import aws_sdk_iotsitewise.types.binding_value_list

        out["list"] = aws_sdk_iotsitewise.types.binding_value_list.deserialize_json(
            data["list"]
        )
    return out
