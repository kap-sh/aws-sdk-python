"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_data_source_item
    import aws_sdk_quicksight.types.geospatial_layer_definition
    import aws_sdk_quicksight.types.geospatial_layer_join_definition
    import aws_sdk_quicksight.types.geospatial_layer_type
    import aws_sdk_quicksight.types.layer_custom_action_list
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visibility


class GeospatialLayerItem(TypedDict, closed=True):
    layer_id: "aws_sdk_quicksight.types.string.String"
    """<p>The ID of the layer.</p>"""
    layer_type: NotRequired[
        "aws_sdk_quicksight.types.geospatial_layer_type.GeospatialLayerType"
    ]
    """<p>The layer type.</p>"""
    data_source: NotRequired[
        "aws_sdk_quicksight.types.geospatial_data_source_item.GeospatialDataSourceItem"
    ]
    """<p>The data source for the layer.</p>"""
    label: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The label that is displayed for the layer.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The state of visibility for the layer.</p>"""
    layer_definition: NotRequired[
        "aws_sdk_quicksight.types.geospatial_layer_definition.GeospatialLayerDefinition"
    ]
    """<p>The definition properties for a layer.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    join_definition: NotRequired[
        "aws_sdk_quicksight.types.geospatial_layer_join_definition.GeospatialLayerJoinDefinition"
    ]
    """<p>The join definition properties for a layer.</p>"""
    actions: NotRequired[
        "aws_sdk_quicksight.types.layer_custom_action_list.LayerCustomActionList"
    ]
    """<p>A list of custom actions for a layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerItem) -> dict:
    out: dict = {}
    out["LayerId"] = value["layer_id"]
    if "layer_type" in value:
        import aws_sdk_quicksight.types.geospatial_layer_type

        out["LayerType"] = (
            aws_sdk_quicksight.types.geospatial_layer_type.serialize_json(
                value["layer_type"]
            )
        )
    if "data_source" in value:
        import aws_sdk_quicksight.types.geospatial_data_source_item

        out["DataSource"] = (
            aws_sdk_quicksight.types.geospatial_data_source_item.serialize_json(
                value["data_source"]
            )
        )
    if "label" in value:
        out["Label"] = value["label"]
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "layer_definition" in value:
        import aws_sdk_quicksight.types.geospatial_layer_definition

        out["LayerDefinition"] = (
            aws_sdk_quicksight.types.geospatial_layer_definition.serialize_json(
                value["layer_definition"]
            )
        )
    if "tooltip" in value:
        import aws_sdk_quicksight.types.tooltip_options

        out["Tooltip"] = aws_sdk_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "join_definition" in value:
        import aws_sdk_quicksight.types.geospatial_layer_join_definition

        out["JoinDefinition"] = (
            aws_sdk_quicksight.types.geospatial_layer_join_definition.serialize_json(
                value["join_definition"]
            )
        )
    if "actions" in value:
        import aws_sdk_quicksight.types.layer_custom_action_list

        out["Actions"] = (
            aws_sdk_quicksight.types.layer_custom_action_list.serialize_json(
                value["actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerItem:
    out: GeospatialLayerItem = {}  # type: ignore[typeddict-item]
    if "LayerId" in data:
        out["layer_id"] = data["LayerId"]
    else:
        raise DeserializationError("GeospatialLayerItem.layer_id required")
    if "LayerType" in data:
        import aws_sdk_quicksight.types.geospatial_layer_type

        out["layer_type"] = (
            aws_sdk_quicksight.types.geospatial_layer_type.deserialize_json(
                data["LayerType"]
            )
        )
    if "DataSource" in data:
        import aws_sdk_quicksight.types.geospatial_data_source_item

        out["data_source"] = (
            aws_sdk_quicksight.types.geospatial_data_source_item.deserialize_json(
                data["DataSource"]
            )
        )
    if "Label" in data:
        out["label"] = data["Label"]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "LayerDefinition" in data:
        import aws_sdk_quicksight.types.geospatial_layer_definition

        out["layer_definition"] = (
            aws_sdk_quicksight.types.geospatial_layer_definition.deserialize_json(
                data["LayerDefinition"]
            )
        )
    if "Tooltip" in data:
        import aws_sdk_quicksight.types.tooltip_options

        out["tooltip"] = aws_sdk_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if "JoinDefinition" in data:
        import aws_sdk_quicksight.types.geospatial_layer_join_definition

        out["join_definition"] = (
            aws_sdk_quicksight.types.geospatial_layer_join_definition.deserialize_json(
                data["JoinDefinition"]
            )
        )
    if "Actions" in data:
        import aws_sdk_quicksight.types.layer_custom_action_list

        out["actions"] = (
            aws_sdk_quicksight.types.layer_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    return out
