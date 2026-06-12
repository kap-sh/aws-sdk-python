"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowStepsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.workflow_step_item

WorkflowStepsList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.workflow_step_item.WorkflowStepItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepsList) -> list:
    import aws_sdk_customer_profiles.types.workflow_step_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.workflow_step_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowStepsList:
    import aws_sdk_customer_profiles.types.workflow_step_item

    out: WorkflowStepsList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.workflow_step_item.deserialize_json(item)
        )
    return out
