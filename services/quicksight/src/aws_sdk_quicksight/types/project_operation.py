"""Generated from Smithy shape ``com.amazonaws.quicksight#ProjectOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.projected_column_name_list
    import aws_sdk_quicksight.types.transform_operation_alias
    import aws_sdk_quicksight.types.transform_operation_source


class ProjectOperation(TypedDict, closed=True):
    alias: NotRequired[
        "aws_sdk_quicksight.types.transform_operation_alias.TransformOperationAlias"
    ]
    """<p>Alias for this operation.</p>"""
    source: NotRequired[
        "aws_sdk_quicksight.types.transform_operation_source.TransformOperationSource"
    ]
    """<p>The source transform operation that provides input data for column projection.</p>"""
    projected_columns: (
        "aws_sdk_quicksight.types.projected_column_name_list.ProjectedColumnNameList"
    )
    """<p>Projected columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectOperation) -> dict:
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
    import aws_sdk_quicksight.types.projected_column_name_list

    out["ProjectedColumns"] = (
        aws_sdk_quicksight.types.projected_column_name_list.serialize_json(
            value["projected_columns"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProjectOperation:
    out: ProjectOperation = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "Source" in data:
        import aws_sdk_quicksight.types.transform_operation_source

        out["source"] = (
            aws_sdk_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    if "ProjectedColumns" in data:
        import aws_sdk_quicksight.types.projected_column_name_list

        out["projected_columns"] = (
            aws_sdk_quicksight.types.projected_column_name_list.deserialize_json(
                data["ProjectedColumns"]
            )
        )
    else:
        raise DeserializationError("ProjectOperation.projected_columns required")
    return out
