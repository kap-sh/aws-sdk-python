"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_configuration
    import aws_sdk_quicksight.types.pivot_group_by_column_name_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source
    import aws_sdk_quicksight.types.value_column_configuration


class PivotOperation(TypedDict, closed=True):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: (
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The source transform operation that provides input data for pivoting.</p>"""
    group_by_column_names: NotRequired[
        "aws_sdk_quicksight.types.pivot_group_by_column_name_list.PivotGroupByColumnNameList"
    ]
    """<p>The list of column names to group by when performing the pivot operation.</p>"""
    value_column_configuration: (
        "aws_sdk_quicksight.types.value_column_configuration.ValueColumnConfiguration"
    )
    """<p>Configuration for how to aggregate values when multiple rows map to the same pivoted column.</p>"""
    pivot_configuration: (
        "aws_sdk_quicksight.types.pivot_configuration.PivotConfiguration"
    )
    """<p>Configuration that specifies which labels to pivot and how to structure the resulting columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.transform_operation_source

    out["Source"] = aws_sdk_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    if "group_by_column_names" in value:
        import aws_sdk_quicksight.types.pivot_group_by_column_name_list

        out["GroupByColumnNames"] = (
            aws_sdk_quicksight.types.pivot_group_by_column_name_list.serialize_json(
                value["group_by_column_names"]
            )
        )
    import aws_sdk_quicksight.types.value_column_configuration

    out["ValueColumnConfiguration"] = (
        aws_sdk_quicksight.types.value_column_configuration.serialize_json(
            value["value_column_configuration"]
        )
    )
    import aws_sdk_quicksight.types.pivot_configuration

    out["PivotConfiguration"] = (
        aws_sdk_quicksight.types.pivot_configuration.serialize_json(
            value["pivot_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PivotOperation:
    out: PivotOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("PivotOperation.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("PivotOperation.source required")
    if "GroupByColumnNames" in data:
        import aws_sdk_quicksight.types.pivot_group_by_column_name_list

        out["group_by_column_names"] = (
            aws_sdk_quicksight.types.pivot_group_by_column_name_list.deserialize_json(
                data["GroupByColumnNames"]
            )
        )
    if "ValueColumnConfiguration" in data:
        import aws_sdk_quicksight.types.value_column_configuration

        out["value_column_configuration"] = (
            aws_sdk_quicksight.types.value_column_configuration.deserialize_json(
                data["ValueColumnConfiguration"]
            )
        )
    else:
        raise DeserializationError("PivotOperation.value_column_configuration required")
    if "PivotConfiguration" in data:
        import aws_sdk_quicksight.types.pivot_configuration

        out["pivot_configuration"] = (
            aws_sdk_quicksight.types.pivot_configuration.deserialize_json(
                data["PivotConfiguration"]
            )
        )
    else:
        raise DeserializationError("PivotOperation.pivot_configuration required")
    return out
