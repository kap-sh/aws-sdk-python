"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFilterPropertyAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.export_filter_output_data_type
    import aws_sdk_neptune_graph.types.export_filter_source_property_name
    import aws_sdk_neptune_graph.types.multi_value_handling_type


class ExportFilterPropertyAttributes(TypedDict):
    output_type: NotRequired[
        "aws_sdk_neptune_graph.types.export_filter_output_data_type.ExportFilterOutputDataType"
    ]
    """<p>Specifies the data type to use for the property in the exported data (e.g. \"String\", \"Int\", \"Float\"). If a type is not provided, the export process will determine the type. If a given property is present as multiple types (e.g. one vertex has \"height\" stored as a double, and another edge has it stored as a string), the type will be of Any type, otherwise, it will be the type of the property as present in vertices.</p>"""
    source_property_name: NotRequired[
        "aws_sdk_neptune_graph.types.export_filter_source_property_name.ExportFilterSourcePropertyName"
    ]
    """<p>The name of the property as it exists in the original graph data. If not provided, it is assumed that the key matches the desired sourcePropertyName.</p>"""
    multi_value_handling: (
        "aws_sdk_neptune_graph.types.multi_value_handling_type.MultiValueHandlingType"
    )
    """<p>Specifies how to handle properties that have multiple values. Can be either <code>TO_LIST</code> to export all values as a list, or <code>PICK_FIRST</code> to export the first value encountered. If not specified, the default value is <code>PICK_FIRST</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilterPropertyAttributes) -> dict:
    out: dict = {}
    if "output_type" in value:
        out["outputType"] = value["output_type"]
    if "source_property_name" in value:
        out["sourcePropertyName"] = value["source_property_name"]
    import aws_sdk_neptune_graph.types.multi_value_handling_type

    out["multiValueHandling"] = (
        aws_sdk_neptune_graph.types.multi_value_handling_type.serialize_json(
            value.get("multi_value_handling", "PICK_FIRST")
        )
    )
    return out


def deserialize_json(data: dict) -> ExportFilterPropertyAttributes:
    out: ExportFilterPropertyAttributes = {}  # type: ignore[typeddict-item]
    if "outputType" in data:
        out["output_type"] = data["outputType"]
    if "sourcePropertyName" in data:
        out["source_property_name"] = data["sourcePropertyName"]
    if "multiValueHandling" in data:
        import aws_sdk_neptune_graph.types.multi_value_handling_type

        out["multi_value_handling"] = (
            aws_sdk_neptune_graph.types.multi_value_handling_type.deserialize_json(
                data["multiValueHandling"]
            )
        )
    else:
        out["multi_value_handling"] = "PICK_FIRST"
    return out
