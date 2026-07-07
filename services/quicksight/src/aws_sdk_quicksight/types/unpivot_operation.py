"""Generated from Smithy shape ``com.amazonaws.quicksight#UnpivotOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_id
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.column_to_unpivot_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class UnpivotOperation(TypedDict, closed=True):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: (
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The source transform operation that provides input data for unpivoting.</p>"""
    columns_to_unpivot: (
        "aws_sdk_quicksight.types.column_to_unpivot_list.ColumnToUnpivotList"
    )
    """<p>The list of columns to unpivot from the source data.</p>"""
    unpivoted_label_column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name for the new column that will contain the unpivoted column names.</p>"""
    unpivoted_label_column_id: "aws_sdk_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the new column that will contain the unpivoted column names.</p>"""
    unpivoted_value_column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name for the new column that will contain the unpivoted values.</p>"""
    unpivoted_value_column_id: "aws_sdk_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the new column that will contain the unpivoted values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnpivotOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.transform_operation_source

    out["Source"] = aws_sdk_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import aws_sdk_quicksight.types.column_to_unpivot_list

    out["ColumnsToUnpivot"] = (
        aws_sdk_quicksight.types.column_to_unpivot_list.serialize_json(
            value["columns_to_unpivot"]
        )
    )
    out["UnpivotedLabelColumnName"] = value["unpivoted_label_column_name"]
    out["UnpivotedLabelColumnId"] = value["unpivoted_label_column_id"]
    out["UnpivotedValueColumnName"] = value["unpivoted_value_column_name"]
    out["UnpivotedValueColumnId"] = value["unpivoted_value_column_id"]
    return out


def deserialize_json(data: dict) -> UnpivotOperation:
    out: UnpivotOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("UnpivotOperation.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("UnpivotOperation.source required")
    if "ColumnsToUnpivot" in data:
        import aws_sdk_quicksight.types.column_to_unpivot_list

        out["columns_to_unpivot"] = (
            aws_sdk_quicksight.types.column_to_unpivot_list.deserialize_json(
                data["ColumnsToUnpivot"]
            )
        )
    else:
        raise DeserializationError("UnpivotOperation.columns_to_unpivot required")
    if "UnpivotedLabelColumnName" in data:
        out["unpivoted_label_column_name"] = data["UnpivotedLabelColumnName"]
    else:
        raise DeserializationError(
            "UnpivotOperation.unpivoted_label_column_name required"
        )
    if "UnpivotedLabelColumnId" in data:
        out["unpivoted_label_column_id"] = data["UnpivotedLabelColumnId"]
    else:
        raise DeserializationError(
            "UnpivotOperation.unpivoted_label_column_id required"
        )
    if "UnpivotedValueColumnName" in data:
        out["unpivoted_value_column_name"] = data["UnpivotedValueColumnName"]
    else:
        raise DeserializationError(
            "UnpivotOperation.unpivoted_value_column_name required"
        )
    if "UnpivotedValueColumnId" in data:
        out["unpivoted_value_column_id"] = data["UnpivotedValueColumnId"]
    else:
        raise DeserializationError(
            "UnpivotOperation.unpivoted_value_column_id required"
        )
    return out
