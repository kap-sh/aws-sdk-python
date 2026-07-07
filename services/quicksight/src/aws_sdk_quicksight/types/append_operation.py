"""Generated from Smithy shape ``com.amazonaws.quicksight#AppendOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.appended_column_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class AppendOperation(TypedDict, closed=True):
    alias: "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    first_source: NotRequired[
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    ]
    """<p>The first data source to be included in the append operation.</p>"""
    second_source: NotRequired[
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    ]
    """<p>The second data source to be appended to the first source.</p>"""
    appended_columns: "aws_sdk_quicksight.types.appended_column_list.AppendedColumnList"
    """<p>The list of columns to include in the appended result, mapping columns from both sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppendOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    if "first_source" in value:
        import aws_sdk_quicksight.types.transform_operation_source

        out["FirstSource"] = (
            aws_sdk_quicksight.types.transform_operation_source.serialize_json(
                value["first_source"]
            )
        )
    if "second_source" in value:
        import aws_sdk_quicksight.types.transform_operation_source

        out["SecondSource"] = (
            aws_sdk_quicksight.types.transform_operation_source.serialize_json(
                value["second_source"]
            )
        )
    import aws_sdk_quicksight.types.appended_column_list

    out["AppendedColumns"] = (
        aws_sdk_quicksight.types.appended_column_list.serialize_json(
            value["appended_columns"]
        )
    )
    return out


def deserialize_json(data: dict) -> AppendOperation:
    out: AppendOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("AppendOperation.alias required")
    if "FirstSource" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["first_source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["FirstSource"]
            )
        )
    if "SecondSource" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["second_source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["SecondSource"]
            )
        )
    if "AppendedColumns" in data:
        import aws_sdk_quicksight.types.appended_column_list

        out["appended_columns"] = (
            aws_sdk_quicksight.types.appended_column_list.deserialize_json(
                data["AppendedColumns"]
            )
        )
    else:
        raise DeserializationError("AppendOperation.appended_columns required")
    return out
