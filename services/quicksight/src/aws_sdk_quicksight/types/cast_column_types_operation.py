"""Generated from Smithy shape ``com.amazonaws.quicksight#CastColumnTypesOperation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cast_column_type_operation_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class CastColumnTypesOperation(TypedDict):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: (
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The source transform operation that provides input data for the type casting.</p>"""
    cast_column_type_operations: "aws_sdk_quicksight.types.cast_column_type_operation_list.CastColumnTypeOperationList"
    """<p>The list of column type casting operations to perform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CastColumnTypesOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.transform_operation_source

    out["Source"] = aws_sdk_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import aws_sdk_quicksight.types.cast_column_type_operation_list

    out["CastColumnTypeOperations"] = (
        aws_sdk_quicksight.types.cast_column_type_operation_list.serialize_json(
            value["cast_column_type_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> CastColumnTypesOperation:
    out: CastColumnTypesOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("CastColumnTypesOperation.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("CastColumnTypesOperation.source required")
    if "CastColumnTypeOperations" in data:
        import aws_sdk_quicksight.types.cast_column_type_operation_list

        out["cast_column_type_operations"] = (
            aws_sdk_quicksight.types.cast_column_type_operation_list.deserialize_json(
                data["CastColumnTypeOperations"]
            )
        )
    else:
        raise DeserializationError(
            "CastColumnTypesOperation.cast_column_type_operations required"
        )
    return out
