"""Generated from Smithy shape ``com.amazonaws.connect#AssociateWorkspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.failed_batch_association_summary_list
    import aws_sdk_connect.types.successful_batch_association_summary_list


class AssociateWorkspaceResponse(TypedDict):
    successful_list: NotRequired[
        "aws_sdk_connect.types.successful_batch_association_summary_list.SuccessfulBatchAssociationSummaryList"
    ]
    """<p>A list of resources that were successfully associated with the workspace.</p>"""
    failed_list: NotRequired[
        "aws_sdk_connect.types.failed_batch_association_summary_list.FailedBatchAssociationSummaryList"
    ]
    """<p>A list of resources that failed to be associated with the workspace, including error details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWorkspaceResponse) -> dict:
    out: dict = {}
    if "successful_list" in value:
        import aws_sdk_connect.types.successful_batch_association_summary_list

        out["SuccessfulList"] = (
            aws_sdk_connect.types.successful_batch_association_summary_list.serialize_json(
                value["successful_list"]
            )
        )
    if "failed_list" in value:
        import aws_sdk_connect.types.failed_batch_association_summary_list

        out["FailedList"] = (
            aws_sdk_connect.types.failed_batch_association_summary_list.serialize_json(
                value["failed_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateWorkspaceResponse:
    out: AssociateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "SuccessfulList" in data:
        import aws_sdk_connect.types.successful_batch_association_summary_list

        out["successful_list"] = (
            aws_sdk_connect.types.successful_batch_association_summary_list.deserialize_json(
                data["SuccessfulList"]
            )
        )
    if "FailedList" in data:
        import aws_sdk_connect.types.failed_batch_association_summary_list

        out["failed_list"] = (
            aws_sdk_connect.types.failed_batch_association_summary_list.deserialize_json(
                data["FailedList"]
            )
        )
    return out
