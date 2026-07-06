"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#BatchGetViewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.batch_get_view_errors
    import aws_sdk_resource_explorer_2.types.view_list


class BatchGetViewOutput(TypedDict, closed=True):
    views: NotRequired["aws_sdk_resource_explorer_2.types.view_list.ViewList"]
    """<p>A structure with a list of objects with details for each of the specified views.</p>"""
    errors: NotRequired[
        "aws_sdk_resource_explorer_2.types.batch_get_view_errors.BatchGetViewErrors"
    ]
    """<p>If any of the specified ARNs result in an error, then this structure describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetViewOutput) -> dict:
    out: dict = {}
    if "views" in value:
        import aws_sdk_resource_explorer_2.types.view_list

        out["Views"] = aws_sdk_resource_explorer_2.types.view_list.serialize_json(
            value["views"]
        )
    if "errors" in value:
        import aws_sdk_resource_explorer_2.types.batch_get_view_errors

        out["Errors"] = (
            aws_sdk_resource_explorer_2.types.batch_get_view_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetViewOutput:
    out: BatchGetViewOutput = {}  # type: ignore[typeddict-item]
    if "Views" in data:
        import aws_sdk_resource_explorer_2.types.view_list

        out["views"] = aws_sdk_resource_explorer_2.types.view_list.deserialize_json(
            data["Views"]
        )
    if "Errors" in data:
        import aws_sdk_resource_explorer_2.types.batch_get_view_errors

        out["errors"] = (
            aws_sdk_resource_explorer_2.types.batch_get_view_errors.deserialize_json(
                data["Errors"]
            )
        )
    return out
