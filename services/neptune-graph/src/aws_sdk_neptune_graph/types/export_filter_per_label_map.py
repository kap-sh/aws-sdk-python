"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFilterPerLabelMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.export_filter_element
    import aws_sdk_neptune_graph.types.export_filter_label

ExportFilterPerLabelMap: TypeAlias = dict[
    "aws_sdk_neptune_graph.types.export_filter_label.ExportFilterLabel",
    "aws_sdk_neptune_graph.types.export_filter_element.ExportFilterElement",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExportFilterPerLabelMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_neptune_graph.types.export_filter_element

        out[key] = aws_sdk_neptune_graph.types.export_filter_element.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ExportFilterPerLabelMap:
    out: ExportFilterPerLabelMap = {}
    for key, value in data.items():
        import aws_sdk_neptune_graph.types.export_filter_element

        out[key] = aws_sdk_neptune_graph.types.export_filter_element.deserialize_json(
            value
        )
    return out
