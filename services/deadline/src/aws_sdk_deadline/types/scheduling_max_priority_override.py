"""Generated from Smithy shape ``com.amazonaws.deadline#SchedulingMaxPriorityOverride``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.scheduling_max_priority_override_always_schedule_first


class _SchedulingMaxPriorityOverride_alwaysScheduleFirst(TypedDict):
    alwaysScheduleFirst: "aws_sdk_deadline.types.scheduling_max_priority_override_always_schedule_first.SchedulingMaxPriorityOverrideAlwaysScheduleFirst"


SchedulingMaxPriorityOverride: TypeAlias = (
    _SchedulingMaxPriorityOverride_alwaysScheduleFirst
)


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingMaxPriorityOverride) -> dict:
    if "alwaysScheduleFirst" in value:
        import aws_sdk_deadline.types.scheduling_max_priority_override_always_schedule_first

        return {
            "alwaysScheduleFirst": aws_sdk_deadline.types.scheduling_max_priority_override_always_schedule_first.serialize_json(
                value["alwaysScheduleFirst"]
            )
        }
    else:
        raise SerializationError("SchedulingMaxPriorityOverride: no variant present")


def deserialize_json(data: dict) -> SchedulingMaxPriorityOverride:
    if "alwaysScheduleFirst" in data:
        import aws_sdk_deadline.types.scheduling_max_priority_override_always_schedule_first

        return {
            "alwaysScheduleFirst": aws_sdk_deadline.types.scheduling_max_priority_override_always_schedule_first.deserialize_json(
                data["alwaysScheduleFirst"]
            )
        }
    else:
        raise DeserializationError(
            "SchedulingMaxPriorityOverride: no recognized variant key"
        )
