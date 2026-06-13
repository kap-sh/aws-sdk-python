"""Generated from Smithy shape ``com.amazonaws.quicksight#FiltersOperation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_operation_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class FiltersOperation(TypedDict):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: (
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The source transform operation that provides input data for filtering.</p>"""
    filter_operations: (
        "aws_sdk_quicksight.types.filter_operation_list.FilterOperationList"
    )
    """<p>The list of filter operations to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FiltersOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import aws_sdk_quicksight.types.transform_operation_source

    out["Source"] = aws_sdk_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import aws_sdk_quicksight.types.filter_operation_list

    out["FilterOperations"] = (
        aws_sdk_quicksight.types.filter_operation_list.serialize_json(
            value["filter_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> FiltersOperation:
    out: FiltersOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("FiltersOperation.alias required")
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("FiltersOperation.source required")
    if "FilterOperations" in data:
        import aws_sdk_quicksight.types.filter_operation_list

        out["filter_operations"] = (
            aws_sdk_quicksight.types.filter_operation_list.deserialize_json(
                data["FilterOperations"]
            )
        )
    else:
        raise DeserializationError("FiltersOperation.filter_operations required")
    return out
