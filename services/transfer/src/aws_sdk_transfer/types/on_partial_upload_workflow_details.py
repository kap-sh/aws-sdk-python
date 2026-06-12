"""Generated from Smithy shape ``com.amazonaws.transfer#OnPartialUploadWorkflowDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.workflow_detail

OnPartialUploadWorkflowDetails: TypeAlias = list[
    "aws_sdk_transfer.types.workflow_detail.WorkflowDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnPartialUploadWorkflowDetails) -> list:
    import aws_sdk_transfer.types.workflow_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_transfer.types.workflow_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OnPartialUploadWorkflowDetails:
    import aws_sdk_transfer.types.workflow_detail

    out: OnPartialUploadWorkflowDetails = []
    for item in data:
        out.append(
            aws_sdk_transfer.types.workflow_detail.deserialize_aws_json_1_1(item)
        )
    return out
