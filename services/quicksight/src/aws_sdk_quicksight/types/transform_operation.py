"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformOperation``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cast_column_type_operation
    import aws_sdk_quicksight.types.create_columns_operation
    import aws_sdk_quicksight.types.filter_operation
    import aws_sdk_quicksight.types.override_dataset_parameter_operation
    import aws_sdk_quicksight.types.project_operation
    import aws_sdk_quicksight.types.rename_column_operation
    import aws_sdk_quicksight.types.tag_column_operation
    import aws_sdk_quicksight.types.untag_column_operation


class _TransformOperation_ProjectOperation(TypedDict):
    ProjectOperation: "aws_sdk_quicksight.types.project_operation.ProjectOperation"


class _TransformOperation_FilterOperation(TypedDict):
    FilterOperation: "aws_sdk_quicksight.types.filter_operation.FilterOperation"


class _TransformOperation_CreateColumnsOperation(TypedDict):
    CreateColumnsOperation: (
        "aws_sdk_quicksight.types.create_columns_operation.CreateColumnsOperation"
    )


class _TransformOperation_RenameColumnOperation(TypedDict):
    RenameColumnOperation: (
        "aws_sdk_quicksight.types.rename_column_operation.RenameColumnOperation"
    )


class _TransformOperation_CastColumnTypeOperation(TypedDict):
    CastColumnTypeOperation: (
        "aws_sdk_quicksight.types.cast_column_type_operation.CastColumnTypeOperation"
    )


class _TransformOperation_TagColumnOperation(TypedDict):
    TagColumnOperation: (
        "aws_sdk_quicksight.types.tag_column_operation.TagColumnOperation"
    )


class _TransformOperation_UntagColumnOperation(TypedDict):
    UntagColumnOperation: (
        "aws_sdk_quicksight.types.untag_column_operation.UntagColumnOperation"
    )


class _TransformOperation_OverrideDatasetParameterOperation(TypedDict):
    OverrideDatasetParameterOperation: "aws_sdk_quicksight.types.override_dataset_parameter_operation.OverrideDatasetParameterOperation"


TransformOperation: TypeAlias = (
    _TransformOperation_ProjectOperation
    | _TransformOperation_FilterOperation
    | _TransformOperation_CreateColumnsOperation
    | _TransformOperation_RenameColumnOperation
    | _TransformOperation_CastColumnTypeOperation
    | _TransformOperation_TagColumnOperation
    | _TransformOperation_UntagColumnOperation
    | _TransformOperation_OverrideDatasetParameterOperation
)


# --- restJson1 ser/de ---
def serialize_json(value: TransformOperation) -> dict:
    if "ProjectOperation" in value:
        import aws_sdk_quicksight.types.project_operation

        return {
            "ProjectOperation": aws_sdk_quicksight.types.project_operation.serialize_json(
                value["ProjectOperation"]
            )
        }
    elif "FilterOperation" in value:
        import aws_sdk_quicksight.types.filter_operation

        return {
            "FilterOperation": aws_sdk_quicksight.types.filter_operation.serialize_json(
                value["FilterOperation"]
            )
        }
    elif "CreateColumnsOperation" in value:
        import aws_sdk_quicksight.types.create_columns_operation

        return {
            "CreateColumnsOperation": aws_sdk_quicksight.types.create_columns_operation.serialize_json(
                value["CreateColumnsOperation"]
            )
        }
    elif "RenameColumnOperation" in value:
        import aws_sdk_quicksight.types.rename_column_operation

        return {
            "RenameColumnOperation": aws_sdk_quicksight.types.rename_column_operation.serialize_json(
                value["RenameColumnOperation"]
            )
        }
    elif "CastColumnTypeOperation" in value:
        import aws_sdk_quicksight.types.cast_column_type_operation

        return {
            "CastColumnTypeOperation": aws_sdk_quicksight.types.cast_column_type_operation.serialize_json(
                value["CastColumnTypeOperation"]
            )
        }
    elif "TagColumnOperation" in value:
        import aws_sdk_quicksight.types.tag_column_operation

        return {
            "TagColumnOperation": aws_sdk_quicksight.types.tag_column_operation.serialize_json(
                value["TagColumnOperation"]
            )
        }
    elif "UntagColumnOperation" in value:
        import aws_sdk_quicksight.types.untag_column_operation

        return {
            "UntagColumnOperation": aws_sdk_quicksight.types.untag_column_operation.serialize_json(
                value["UntagColumnOperation"]
            )
        }
    elif "OverrideDatasetParameterOperation" in value:
        import aws_sdk_quicksight.types.override_dataset_parameter_operation

        return {
            "OverrideDatasetParameterOperation": aws_sdk_quicksight.types.override_dataset_parameter_operation.serialize_json(
                value["OverrideDatasetParameterOperation"]
            )
        }
    else:
        raise SerializationError("TransformOperation: no variant present")


def deserialize_json(data: dict) -> TransformOperation:
    if "ProjectOperation" in data:
        import aws_sdk_quicksight.types.project_operation

        return {
            "ProjectOperation": aws_sdk_quicksight.types.project_operation.deserialize_json(
                data["ProjectOperation"]
            )
        }
    elif "FilterOperation" in data:
        import aws_sdk_quicksight.types.filter_operation

        return {
            "FilterOperation": aws_sdk_quicksight.types.filter_operation.deserialize_json(
                data["FilterOperation"]
            )
        }
    elif "CreateColumnsOperation" in data:
        import aws_sdk_quicksight.types.create_columns_operation

        return {
            "CreateColumnsOperation": aws_sdk_quicksight.types.create_columns_operation.deserialize_json(
                data["CreateColumnsOperation"]
            )
        }
    elif "RenameColumnOperation" in data:
        import aws_sdk_quicksight.types.rename_column_operation

        return {
            "RenameColumnOperation": aws_sdk_quicksight.types.rename_column_operation.deserialize_json(
                data["RenameColumnOperation"]
            )
        }
    elif "CastColumnTypeOperation" in data:
        import aws_sdk_quicksight.types.cast_column_type_operation

        return {
            "CastColumnTypeOperation": aws_sdk_quicksight.types.cast_column_type_operation.deserialize_json(
                data["CastColumnTypeOperation"]
            )
        }
    elif "TagColumnOperation" in data:
        import aws_sdk_quicksight.types.tag_column_operation

        return {
            "TagColumnOperation": aws_sdk_quicksight.types.tag_column_operation.deserialize_json(
                data["TagColumnOperation"]
            )
        }
    elif "UntagColumnOperation" in data:
        import aws_sdk_quicksight.types.untag_column_operation

        return {
            "UntagColumnOperation": aws_sdk_quicksight.types.untag_column_operation.deserialize_json(
                data["UntagColumnOperation"]
            )
        }
    elif "OverrideDatasetParameterOperation" in data:
        import aws_sdk_quicksight.types.override_dataset_parameter_operation

        return {
            "OverrideDatasetParameterOperation": aws_sdk_quicksight.types.override_dataset_parameter_operation.deserialize_json(
                data["OverrideDatasetParameterOperation"]
            )
        }
    else:
        raise DeserializationError("TransformOperation: no recognized variant key")
