"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.export_filter_per_label_map


class ExportFilter(TypedDict):
    vertex_filter: NotRequired[
        "aws_sdk_neptune_graph.types.export_filter_per_label_map.ExportFilterPerLabelMap"
    ]
    """<p>Used to specify filters on a per-label basis for vertices. This allows you to control which vertex labels and properties are included in the export.</p>"""
    edge_filter: NotRequired[
        "aws_sdk_neptune_graph.types.export_filter_per_label_map.ExportFilterPerLabelMap"
    ]
    """<p>Used to specify filters on a per-label basis for edges. This allows you to control which edge labels and properties are included in the export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilter) -> dict:
    out: dict = {}
    if "vertex_filter" in value:
        import aws_sdk_neptune_graph.types.export_filter_per_label_map

        out["vertexFilter"] = (
            aws_sdk_neptune_graph.types.export_filter_per_label_map.serialize_json(
                value["vertex_filter"]
            )
        )
    if "edge_filter" in value:
        import aws_sdk_neptune_graph.types.export_filter_per_label_map

        out["edgeFilter"] = (
            aws_sdk_neptune_graph.types.export_filter_per_label_map.serialize_json(
                value["edge_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportFilter:
    out: ExportFilter = {}  # type: ignore[typeddict-item]
    if "vertexFilter" in data:
        import aws_sdk_neptune_graph.types.export_filter_per_label_map

        out["vertex_filter"] = (
            aws_sdk_neptune_graph.types.export_filter_per_label_map.deserialize_json(
                data["vertexFilter"]
            )
        )
    if "edgeFilter" in data:
        import aws_sdk_neptune_graph.types.export_filter_per_label_map

        out["edge_filter"] = (
            aws_sdk_neptune_graph.types.export_filter_per_label_map.deserialize_json(
                data["edgeFilter"]
            )
        )
    return out
