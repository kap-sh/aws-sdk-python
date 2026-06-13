"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregateOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_list
    import aws_sdk_quicksight.types.group_by_column_name_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class AggregateOperation(TypedDict):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: (
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The source transform operation that provides input data for the aggregation.</p>"""
    group_by_column_names: NotRequired[
        "aws_sdk_quicksight.types.group_by_column_name_list.GroupByColumnNameList"
    ]
    """<p>The list of column names to group by when performing the aggregation. Rows with the same values in these columns will be grouped together.</p>"""
    aggregations: "aws_sdk_quicksight.types.aggregation_list.AggregationList"
    """<p>The list of aggregation functions to apply to the grouped data, such as <code>SUM</code>, <code>COUNT</code>, or <code>AVERAGE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregateOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.transform_operation_source

    out["Source"] = aws_sdk_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    if "group_by_column_names" in value:
        import aws_sdk_quicksight.types.group_by_column_name_list

        out["GroupByColumnNames"] = (
            aws_sdk_quicksight.types.group_by_column_name_list.serialize_json(
                value["group_by_column_names"]
            )
        )
    import aws_sdk_quicksight.types.aggregation_list

    out["Aggregations"] = aws_sdk_quicksight.types.aggregation_list.serialize_json(
        value["aggregations"]
    )
    return out


def deserialize_json(data: dict) -> AggregateOperation:
    out: AggregateOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("AggregateOperation.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("AggregateOperation.source required")
    if "GroupByColumnNames" in data:
        import aws_sdk_quicksight.types.group_by_column_name_list

        out["group_by_column_names"] = (
            aws_sdk_quicksight.types.group_by_column_name_list.deserialize_json(
                data["GroupByColumnNames"]
            )
        )
    if "Aggregations" in data:
        import aws_sdk_quicksight.types.aggregation_list

        out["aggregations"] = (
            aws_sdk_quicksight.types.aggregation_list.deserialize_json(
                data["Aggregations"]
            )
        )
    else:
        raise DeserializationError("AggregateOperation.aggregations required")
    return out
