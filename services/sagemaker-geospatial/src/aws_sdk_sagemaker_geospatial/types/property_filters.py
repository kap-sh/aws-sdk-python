"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#PropertyFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.logical_operator
    import aws_sdk_sagemaker_geospatial.types.property_filters_list


class PropertyFilters(TypedDict):
    properties: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.property_filters_list.PropertyFiltersList"
    ]
    """<p>A list of Property Filters.</p>"""
    logical_operator: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.logical_operator.LogicalOperator"
    ]
    """<p>The Logical Operator used to combine the Property Filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyFilters) -> dict:
    out: dict = {}
    if "properties" in value:
        import aws_sdk_sagemaker_geospatial.types.property_filters_list

        out["Properties"] = (
            aws_sdk_sagemaker_geospatial.types.property_filters_list.serialize_json(
                value["properties"]
            )
        )
    if "logical_operator" in value:
        out["LogicalOperator"] = value["logical_operator"]
    return out


def deserialize_json(data: dict) -> PropertyFilters:
    out: PropertyFilters = {}  # type: ignore[typeddict-item]
    if "Properties" in data:
        import aws_sdk_sagemaker_geospatial.types.property_filters_list

        out["properties"] = (
            aws_sdk_sagemaker_geospatial.types.property_filters_list.deserialize_json(
                data["Properties"]
            )
        )
    if "LogicalOperator" in data:
        out["logical_operator"] = data["LogicalOperator"]
    return out
