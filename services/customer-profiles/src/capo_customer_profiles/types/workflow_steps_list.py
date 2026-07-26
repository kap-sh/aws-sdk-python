"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowStepsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.workflow_step_item

WorkflowStepsList: TypeAlias = list[
    "capo_customer_profiles.types.workflow_step_item.WorkflowStepItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepsList) -> list:
    import capo_customer_profiles.types.workflow_step_item

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.workflow_step_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkflowStepsList:
    import capo_customer_profiles.types.workflow_step_item

    out: WorkflowStepsList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.workflow_step_item.deserialize_json(item)
        )
    return out
