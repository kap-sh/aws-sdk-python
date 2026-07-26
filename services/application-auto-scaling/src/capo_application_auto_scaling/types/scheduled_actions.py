"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScheduledActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.scheduled_action

ScheduledActions: TypeAlias = list[
    "capo_application_auto_scaling.types.scheduled_action.ScheduledAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledActions) -> list:
    import capo_application_auto_scaling.types.scheduled_action

    out: list = []
    for item in value:
        out.append(
            capo_application_auto_scaling.types.scheduled_action.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScheduledActions:
    import capo_application_auto_scaling.types.scheduled_action

    out: ScheduledActions = []
    for item in data:
        out.append(
            capo_application_auto_scaling.types.scheduled_action.deserialize_aws_json_1_1(
                item
            )
        )
    return out
