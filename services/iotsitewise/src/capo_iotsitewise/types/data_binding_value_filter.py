"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataBindingValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_binding_value_filter
    import capo_iotsitewise.types.asset_model_binding_value_filter
    import capo_iotsitewise.types.asset_model_property_binding_value_filter
    import capo_iotsitewise.types.asset_property_binding_value_filter


class DataBindingValueFilter(TypedDict, closed=True):
    asset: NotRequired[
        "capo_iotsitewise.types.asset_binding_value_filter.AssetBindingValueFilter"
    ]
    """<p>Filter criteria for matching data bindings based on a specific asset. Used to list all data bindings referencing a particular asset or its properties.</p>"""
    asset_model: NotRequired[
        "capo_iotsitewise.types.asset_model_binding_value_filter.AssetModelBindingValueFilter"
    ]
    """<p>Filter criteria for matching data bindings based on a specific asset model. Used to list all data bindings referencing a particular asset model or its properties.</p>"""
    asset_property: NotRequired[
        "capo_iotsitewise.types.asset_property_binding_value_filter.AssetPropertyBindingValueFilter"
    ]
    """<p>Filter criteria for matching data bindings based on a specific asset property. Used to list all data bindings referencing a particular property of an asset.</p>"""
    asset_model_property: NotRequired[
        "capo_iotsitewise.types.asset_model_property_binding_value_filter.AssetModelPropertyBindingValueFilter"
    ]
    """<p>Filter criteria for matching data bindings based on a specific asset model property. Used to list all data bindings referencing a particular property of an asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataBindingValueFilter) -> dict:
    out: dict = {}
    if "asset" in value:
        import capo_iotsitewise.types.asset_binding_value_filter

        out["asset"] = capo_iotsitewise.types.asset_binding_value_filter.serialize_json(
            value["asset"]
        )
    if "asset_model" in value:
        import capo_iotsitewise.types.asset_model_binding_value_filter

        out["assetModel"] = (
            capo_iotsitewise.types.asset_model_binding_value_filter.serialize_json(
                value["asset_model"]
            )
        )
    if "asset_property" in value:
        import capo_iotsitewise.types.asset_property_binding_value_filter

        out["assetProperty"] = (
            capo_iotsitewise.types.asset_property_binding_value_filter.serialize_json(
                value["asset_property"]
            )
        )
    if "asset_model_property" in value:
        import capo_iotsitewise.types.asset_model_property_binding_value_filter

        out["assetModelProperty"] = (
            capo_iotsitewise.types.asset_model_property_binding_value_filter.serialize_json(
                value["asset_model_property"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataBindingValueFilter:
    out: DataBindingValueFilter = {}  # type: ignore[typeddict-item]
    if "asset" in data:
        import capo_iotsitewise.types.asset_binding_value_filter

        out["asset"] = (
            capo_iotsitewise.types.asset_binding_value_filter.deserialize_json(
                data["asset"]
            )
        )
    if "assetModel" in data:
        import capo_iotsitewise.types.asset_model_binding_value_filter

        out["asset_model"] = (
            capo_iotsitewise.types.asset_model_binding_value_filter.deserialize_json(
                data["assetModel"]
            )
        )
    if "assetProperty" in data:
        import capo_iotsitewise.types.asset_property_binding_value_filter

        out["asset_property"] = (
            capo_iotsitewise.types.asset_property_binding_value_filter.deserialize_json(
                data["assetProperty"]
            )
        )
    if "assetModelProperty" in data:
        import capo_iotsitewise.types.asset_model_property_binding_value_filter

        out["asset_model_property"] = (
            capo_iotsitewise.types.asset_model_property_binding_value_filter.deserialize_json(
                data["assetModelProperty"]
            )
        )
    return out
