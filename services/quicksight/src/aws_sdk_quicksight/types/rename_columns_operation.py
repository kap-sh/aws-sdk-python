"""Generated from Smithy shape ``com.amazonaws.quicksight#RenameColumnsOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.rename_column_operation_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class RenameColumnsOperation(TypedDict, closed=True):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: (
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The source transform operation that provides input data for column renaming.</p>"""
    rename_column_operations: "aws_sdk_quicksight.types.rename_column_operation_list.RenameColumnOperationList"
    """<p>The list of column rename operations to perform, specifying old and new column names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenameColumnsOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.transform_operation_source

    out["Source"] = aws_sdk_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import aws_sdk_quicksight.types.rename_column_operation_list

    out["RenameColumnOperations"] = (
        aws_sdk_quicksight.types.rename_column_operation_list.serialize_json(
            value["rename_column_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> RenameColumnsOperation:
    out: RenameColumnsOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("RenameColumnsOperation.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("RenameColumnsOperation.source required")
    if "RenameColumnOperations" in data:
        import aws_sdk_quicksight.types.rename_column_operation_list

        out["rename_column_operations"] = (
            aws_sdk_quicksight.types.rename_column_operation_list.deserialize_json(
                data["RenameColumnOperations"]
            )
        )
    else:
        raise DeserializationError(
            "RenameColumnsOperation.rename_column_operations required"
        )
    return out
