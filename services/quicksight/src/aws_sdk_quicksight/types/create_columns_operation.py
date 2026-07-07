"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateColumnsOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.calculated_column_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class CreateColumnsOperation(TypedDict, closed=True):
    alias: NotRequired[
        "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    ]
    """<p>Alias for this operation.</p>"""
    source: NotRequired[
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    ]
    """<p>The source transform operation that provides input data for creating new calculated columns.</p>"""
    columns: "aws_sdk_quicksight.types.calculated_column_list.CalculatedColumnList"
    """<p>Calculated columns to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateColumnsOperation) -> dict:
    out: dict = {}
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "source" in value:
        import aws_sdk_quicksight.types.transform_operation_source

        out["Source"] = (
            aws_sdk_quicksight.types.transform_operation_source.serialize_json(
                value["source"]
            )
        )
    import aws_sdk_quicksight.types.calculated_column_list

    out["Columns"] = aws_sdk_quicksight.types.calculated_column_list.serialize_json(
        value["columns"]
    )
    return out


def deserialize_json(data: dict) -> CreateColumnsOperation:
    out: CreateColumnsOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    if "Columns" in data:
        import aws_sdk_quicksight.types.calculated_column_list

        out["columns"] = (
            aws_sdk_quicksight.types.calculated_column_list.deserialize_json(
                data["Columns"]
            )
        )
    else:
        raise DeserializationError("CreateColumnsOperation.columns required")
    return out
