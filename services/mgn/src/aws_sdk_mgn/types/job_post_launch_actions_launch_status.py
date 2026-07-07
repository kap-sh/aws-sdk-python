"""Generated from Smithy shape ``com.amazonaws.mgn#JobPostLaunchActionsLaunchStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.post_launch_action_execution_status
    import aws_sdk_mgn.types.ssm_document
    import aws_sdk_mgn.types.ssm_document_type


class JobPostLaunchActionsLaunchStatus(TypedDict, closed=True):
    ssm_document: NotRequired["aws_sdk_mgn.types.ssm_document.SsmDocument"]
    """<p>AWS Systems Manager's Document of the of the Job Post Launch Actions.</p>"""
    ssm_document_type: NotRequired[
        "aws_sdk_mgn.types.ssm_document_type.SsmDocumentType"
    ]
    """<p>AWS Systems Manager Document type.</p>"""
    execution_id: NotRequired["aws_sdk_mgn.types.bounded_string.BoundedString"]
    """<p>AWS Systems Manager Document's execution ID of the of the Job Post Launch Actions.</p>"""
    execution_status: NotRequired[
        "aws_sdk_mgn.types.post_launch_action_execution_status.PostLaunchActionExecutionStatus"
    ]
    """<p>AWS Systems Manager Document's execution status.</p>"""
    failure_reason: NotRequired["aws_sdk_mgn.types.bounded_string.BoundedString"]
    """<p>AWS Systems Manager Document's failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobPostLaunchActionsLaunchStatus) -> dict:
    out: dict = {}
    if "ssm_document" in value:
        import aws_sdk_mgn.types.ssm_document

        out["ssmDocument"] = aws_sdk_mgn.types.ssm_document.serialize_json(
            value["ssm_document"]
        )
    if "ssm_document_type" in value:
        out["ssmDocumentType"] = value["ssm_document_type"]
    if "execution_id" in value:
        out["executionID"] = value["execution_id"]
    if "execution_status" in value:
        out["executionStatus"] = value["execution_status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> JobPostLaunchActionsLaunchStatus:
    out: JobPostLaunchActionsLaunchStatus = {}  # type: ignore[typeddict-item]
    if "ssmDocument" in data:
        import aws_sdk_mgn.types.ssm_document

        out["ssm_document"] = aws_sdk_mgn.types.ssm_document.deserialize_json(
            data["ssmDocument"]
        )
    if "ssmDocumentType" in data:
        out["ssm_document_type"] = data["ssmDocumentType"]
    if "executionID" in data:
        out["execution_id"] = data["executionID"]
    if "executionStatus" in data:
        out["execution_status"] = data["executionStatus"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
