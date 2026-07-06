"""Generated from Smithy shape ``com.amazonaws.deadline#SchedulingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.priority_balanced_scheduling_configuration
    import aws_sdk_deadline.types.priority_fifo_scheduling_configuration
    import aws_sdk_deadline.types.weighted_balanced_scheduling_configuration


class _SchedulingConfiguration_priorityFifo(TypedDict, closed=True):
    priorityFifo: "aws_sdk_deadline.types.priority_fifo_scheduling_configuration.PriorityFifoSchedulingConfiguration"


class _SchedulingConfiguration_priorityBalanced(TypedDict, closed=True):
    priorityBalanced: "aws_sdk_deadline.types.priority_balanced_scheduling_configuration.PriorityBalancedSchedulingConfiguration"


class _SchedulingConfiguration_weightedBalanced(TypedDict, closed=True):
    weightedBalanced: "aws_sdk_deadline.types.weighted_balanced_scheduling_configuration.WeightedBalancedSchedulingConfiguration"


SchedulingConfiguration: TypeAlias = (
    _SchedulingConfiguration_priorityFifo
    | _SchedulingConfiguration_priorityBalanced
    | _SchedulingConfiguration_weightedBalanced
)


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingConfiguration) -> dict:
    if "priorityFifo" in value:
        import aws_sdk_deadline.types.priority_fifo_scheduling_configuration

        return {
            "priorityFifo": aws_sdk_deadline.types.priority_fifo_scheduling_configuration.serialize_json(
                value["priorityFifo"]
            )
        }
    elif "priorityBalanced" in value:
        import aws_sdk_deadline.types.priority_balanced_scheduling_configuration

        return {
            "priorityBalanced": aws_sdk_deadline.types.priority_balanced_scheduling_configuration.serialize_json(
                value["priorityBalanced"]
            )
        }
    elif "weightedBalanced" in value:
        import aws_sdk_deadline.types.weighted_balanced_scheduling_configuration

        return {
            "weightedBalanced": aws_sdk_deadline.types.weighted_balanced_scheduling_configuration.serialize_json(
                value["weightedBalanced"]
            )
        }
    else:
        raise SerializationError("SchedulingConfiguration: no variant present")


def deserialize_json(data: dict) -> SchedulingConfiguration:
    if "priorityFifo" in data:
        import aws_sdk_deadline.types.priority_fifo_scheduling_configuration

        return {
            "priorityFifo": aws_sdk_deadline.types.priority_fifo_scheduling_configuration.deserialize_json(
                data["priorityFifo"]
            )
        }
    elif "priorityBalanced" in data:
        import aws_sdk_deadline.types.priority_balanced_scheduling_configuration

        return {
            "priorityBalanced": aws_sdk_deadline.types.priority_balanced_scheduling_configuration.deserialize_json(
                data["priorityBalanced"]
            )
        }
    elif "weightedBalanced" in data:
        import aws_sdk_deadline.types.weighted_balanced_scheduling_configuration

        return {
            "weightedBalanced": aws_sdk_deadline.types.weighted_balanced_scheduling_configuration.deserialize_json(
                data["weightedBalanced"]
            )
        }
    else:
        raise DeserializationError("SchedulingConfiguration: no recognized variant key")
