"""Generated from Smithy shape ``com.amazonaws.deadline#SchedulingMinPriorityOverride``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_deadline.types.scheduling_min_priority_override_always_schedule_last


class _SchedulingMinPriorityOverride_alwaysScheduleLast(TypedDict, closed=True):
    alwaysScheduleLast: "capo_deadline.types.scheduling_min_priority_override_always_schedule_last.SchedulingMinPriorityOverrideAlwaysScheduleLast"


SchedulingMinPriorityOverride: TypeAlias = (
    _SchedulingMinPriorityOverride_alwaysScheduleLast
)


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingMinPriorityOverride) -> dict:
    if "alwaysScheduleLast" in value:
        import capo_deadline.types.scheduling_min_priority_override_always_schedule_last

        return {
            "alwaysScheduleLast": capo_deadline.types.scheduling_min_priority_override_always_schedule_last.serialize_json(
                value["alwaysScheduleLast"]
            )
        }
    else:
        raise SerializationError("SchedulingMinPriorityOverride: no variant present")


def deserialize_json(data: dict) -> SchedulingMinPriorityOverride:
    if "alwaysScheduleLast" in data:
        import capo_deadline.types.scheduling_min_priority_override_always_schedule_last

        return {
            "alwaysScheduleLast": capo_deadline.types.scheduling_min_priority_override_always_schedule_last.deserialize_json(
                data["alwaysScheduleLast"]
            )
        }
    else:
        raise DeserializationError(
            "SchedulingMinPriorityOverride: no recognized variant key"
        )
