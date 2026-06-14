"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFilterElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.export_filter_property_map


class ExportFilterElement(TypedDict):
    properties: NotRequired[
        "aws_sdk_neptune_graph.types.export_filter_property_map.ExportFilterPropertyMap"
    ]
    r"""<p>Each property is defined by a key-value pair, where the key is the desired output property name (e.g. \"name\"), and the value is an object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilterElement) -> dict:
    out: dict = {}
    if "properties" in value:
        import aws_sdk_neptune_graph.types.export_filter_property_map

        out["properties"] = (
            aws_sdk_neptune_graph.types.export_filter_property_map.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportFilterElement:
    out: ExportFilterElement = {}  # type: ignore[typeddict-item]
    if "properties" in data:
        import aws_sdk_neptune_graph.types.export_filter_property_map

        out["properties"] = (
            aws_sdk_neptune_graph.types.export_filter_property_map.deserialize_json(
                data["properties"]
            )
        )
    return out
