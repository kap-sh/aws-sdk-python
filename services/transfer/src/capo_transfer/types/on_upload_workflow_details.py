"""Generated from Smithy shape ``com.amazonaws.transfer#OnUploadWorkflowDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.workflow_detail

OnUploadWorkflowDetails: TypeAlias = list[
    "capo_transfer.types.workflow_detail.WorkflowDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnUploadWorkflowDetails) -> list:
    import capo_transfer.types.workflow_detail

    out: list = []
    for item in value:
        out.append(capo_transfer.types.workflow_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OnUploadWorkflowDetails:
    import capo_transfer.types.workflow_detail

    out: OnUploadWorkflowDetails = []
    for item in data:
        out.append(capo_transfer.types.workflow_detail.deserialize_aws_json_1_1(item))
    return out
