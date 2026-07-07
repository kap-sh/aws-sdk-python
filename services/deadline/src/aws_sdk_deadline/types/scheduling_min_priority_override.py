"""Generated from Smithy shape ``com.amazonaws.deadline#SchedulingMinPriorityOverride``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.scheduling_min_priority_override_always_schedule_last


class _SchedulingMinPriorityOverride_alwaysScheduleLast(TypedDict, closed=True):
    alwaysScheduleLast: "aws_sdk_deadline.types.scheduling_min_priority_override_always_schedule_last.SchedulingMinPriorityOverrideAlwaysScheduleLast"


SchedulingMinPriorityOverride: TypeAlias = (
    _SchedulingMinPriorityOverride_alwaysScheduleLast
)


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingMinPriorityOverride) -> dict:
    if "alwaysScheduleLast" in value:
        import aws_sdk_deadline.types.scheduling_min_priority_override_always_schedule_last

        return {
            "alwaysScheduleLast": aws_sdk_deadline.types.scheduling_min_priority_override_always_schedule_last.serialize_json(
                value["alwaysScheduleLast"]
            )
        }
    else:
        raise SerializationError("SchedulingMinPriorityOverride: no variant present")


def deserialize_json(data: dict) -> SchedulingMinPriorityOverride:
    if "alwaysScheduleLast" in data:
        import aws_sdk_deadline.types.scheduling_min_priority_override_always_schedule_last

        return {
            "alwaysScheduleLast": aws_sdk_deadline.types.scheduling_min_priority_override_always_schedule_last.deserialize_json(
                data["alwaysScheduleLast"]
            )
        }
    else:
        raise DeserializationError(
            "SchedulingMinPriorityOverride: no recognized variant key"
        )
