"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#IndexStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.error_details
    import aws_sdk_resource_explorer_2.types.index
    import aws_sdk_resource_explorer_2.types.operation_status


class IndexStatus(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_resource_explorer_2.types.operation_status.OperationStatus"
    ]
    """<p>The current status of the index operation. Valid values are <code>SUCCEEDED</code>, <code>FAILED</code>, <code>IN_PROGRESS</code>, or <code>SKIPPED</code>.</p>"""
    index: NotRequired["aws_sdk_resource_explorer_2.types.index.Index"]
    error_details: NotRequired[
        "aws_sdk_resource_explorer_2.types.error_details.ErrorDetails"
    ]
    """<p>Details about any error that occurred during the index operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexStatus) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "index" in value:
        import aws_sdk_resource_explorer_2.types.index

        out["Index"] = aws_sdk_resource_explorer_2.types.index.serialize_json(
            value["index"]
        )
    if "error_details" in value:
        import aws_sdk_resource_explorer_2.types.error_details

        out["ErrorDetails"] = (
            aws_sdk_resource_explorer_2.types.error_details.serialize_json(
                value["error_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> IndexStatus:
    out: IndexStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Index" in data:
        import aws_sdk_resource_explorer_2.types.index

        out["index"] = aws_sdk_resource_explorer_2.types.index.deserialize_json(
            data["Index"]
        )
    if "ErrorDetails" in data:
        import aws_sdk_resource_explorer_2.types.error_details

        out["error_details"] = (
            aws_sdk_resource_explorer_2.types.error_details.deserialize_json(
                data["ErrorDetails"]
            )
        )
    return out
