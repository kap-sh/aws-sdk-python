"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFilterPropertyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptune_graph.types.export_filter_output_property_name
    import capo_neptune_graph.types.export_filter_property_attributes

ExportFilterPropertyMap: TypeAlias = dict[
    "capo_neptune_graph.types.export_filter_output_property_name.ExportFilterOutputPropertyName",
    "capo_neptune_graph.types.export_filter_property_attributes.ExportFilterPropertyAttributes",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExportFilterPropertyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_neptune_graph.types.export_filter_property_attributes

        out[key] = (
            capo_neptune_graph.types.export_filter_property_attributes.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ExportFilterPropertyMap:
    out: ExportFilterPropertyMap = {}
    for key, value in data.items():
        import capo_neptune_graph.types.export_filter_property_attributes

        out[key] = (
            capo_neptune_graph.types.export_filter_property_attributes.deserialize_json(
                value
            )
        )
    return out
