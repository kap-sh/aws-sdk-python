"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformOperation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_quicksight.types.cast_column_type_operation
    import capo_quicksight.types.create_columns_operation
    import capo_quicksight.types.filter_operation
    import capo_quicksight.types.override_dataset_parameter_operation
    import capo_quicksight.types.project_operation
    import capo_quicksight.types.rename_column_operation
    import capo_quicksight.types.tag_column_operation
    import capo_quicksight.types.untag_column_operation


class _TransformOperation_ProjectOperation(TypedDict, closed=True):
    ProjectOperation: "capo_quicksight.types.project_operation.ProjectOperation"


class _TransformOperation_FilterOperation(TypedDict, closed=True):
    FilterOperation: "capo_quicksight.types.filter_operation.FilterOperation"


class _TransformOperation_CreateColumnsOperation(TypedDict, closed=True):
    CreateColumnsOperation: (
        "capo_quicksight.types.create_columns_operation.CreateColumnsOperation"
    )


class _TransformOperation_RenameColumnOperation(TypedDict, closed=True):
    RenameColumnOperation: (
        "capo_quicksight.types.rename_column_operation.RenameColumnOperation"
    )


class _TransformOperation_CastColumnTypeOperation(TypedDict, closed=True):
    CastColumnTypeOperation: (
        "capo_quicksight.types.cast_column_type_operation.CastColumnTypeOperation"
    )


class _TransformOperation_TagColumnOperation(TypedDict, closed=True):
    TagColumnOperation: "capo_quicksight.types.tag_column_operation.TagColumnOperation"


class _TransformOperation_UntagColumnOperation(TypedDict, closed=True):
    UntagColumnOperation: (
        "capo_quicksight.types.untag_column_operation.UntagColumnOperation"
    )


class _TransformOperation_OverrideDatasetParameterOperation(TypedDict, closed=True):
    OverrideDatasetParameterOperation: "capo_quicksight.types.override_dataset_parameter_operation.OverrideDatasetParameterOperation"


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
        import capo_quicksight.types.project_operation

        return {
            "ProjectOperation": capo_quicksight.types.project_operation.serialize_json(
                value["ProjectOperation"]
            )
        }
    elif "FilterOperation" in value:
        import capo_quicksight.types.filter_operation

        return {
            "FilterOperation": capo_quicksight.types.filter_operation.serialize_json(
                value["FilterOperation"]
            )
        }
    elif "CreateColumnsOperation" in value:
        import capo_quicksight.types.create_columns_operation

        return {
            "CreateColumnsOperation": capo_quicksight.types.create_columns_operation.serialize_json(
                value["CreateColumnsOperation"]
            )
        }
    elif "RenameColumnOperation" in value:
        import capo_quicksight.types.rename_column_operation

        return {
            "RenameColumnOperation": capo_quicksight.types.rename_column_operation.serialize_json(
                value["RenameColumnOperation"]
            )
        }
    elif "CastColumnTypeOperation" in value:
        import capo_quicksight.types.cast_column_type_operation

        return {
            "CastColumnTypeOperation": capo_quicksight.types.cast_column_type_operation.serialize_json(
                value["CastColumnTypeOperation"]
            )
        }
    elif "TagColumnOperation" in value:
        import capo_quicksight.types.tag_column_operation

        return {
            "TagColumnOperation": capo_quicksight.types.tag_column_operation.serialize_json(
                value["TagColumnOperation"]
            )
        }
    elif "UntagColumnOperation" in value:
        import capo_quicksight.types.untag_column_operation

        return {
            "UntagColumnOperation": capo_quicksight.types.untag_column_operation.serialize_json(
                value["UntagColumnOperation"]
            )
        }
    elif "OverrideDatasetParameterOperation" in value:
        import capo_quicksight.types.override_dataset_parameter_operation

        return {
            "OverrideDatasetParameterOperation": capo_quicksight.types.override_dataset_parameter_operation.serialize_json(
                value["OverrideDatasetParameterOperation"]
            )
        }
    else:
        raise SerializationError("TransformOperation: no variant present")


def deserialize_json(data: dict) -> TransformOperation:
    if "ProjectOperation" in data:
        import capo_quicksight.types.project_operation

        return {
            "ProjectOperation": capo_quicksight.types.project_operation.deserialize_json(
                data["ProjectOperation"]
            )
        }
    elif "FilterOperation" in data:
        import capo_quicksight.types.filter_operation

        return {
            "FilterOperation": capo_quicksight.types.filter_operation.deserialize_json(
                data["FilterOperation"]
            )
        }
    elif "CreateColumnsOperation" in data:
        import capo_quicksight.types.create_columns_operation

        return {
            "CreateColumnsOperation": capo_quicksight.types.create_columns_operation.deserialize_json(
                data["CreateColumnsOperation"]
            )
        }
    elif "RenameColumnOperation" in data:
        import capo_quicksight.types.rename_column_operation

        return {
            "RenameColumnOperation": capo_quicksight.types.rename_column_operation.deserialize_json(
                data["RenameColumnOperation"]
            )
        }
    elif "CastColumnTypeOperation" in data:
        import capo_quicksight.types.cast_column_type_operation

        return {
            "CastColumnTypeOperation": capo_quicksight.types.cast_column_type_operation.deserialize_json(
                data["CastColumnTypeOperation"]
            )
        }
    elif "TagColumnOperation" in data:
        import capo_quicksight.types.tag_column_operation

        return {
            "TagColumnOperation": capo_quicksight.types.tag_column_operation.deserialize_json(
                data["TagColumnOperation"]
            )
        }
    elif "UntagColumnOperation" in data:
        import capo_quicksight.types.untag_column_operation

        return {
            "UntagColumnOperation": capo_quicksight.types.untag_column_operation.deserialize_json(
                data["UntagColumnOperation"]
            )
        }
    elif "OverrideDatasetParameterOperation" in data:
        import capo_quicksight.types.override_dataset_parameter_operation

        return {
            "OverrideDatasetParameterOperation": capo_quicksight.types.override_dataset_parameter_operation.deserialize_json(
                data["OverrideDatasetParameterOperation"]
            )
        }
    else:
        raise DeserializationError("TransformOperation: no recognized variant key")
