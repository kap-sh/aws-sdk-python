"""Generated from Smithy shape ``com.amazonaws.deadline#StepConsumers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_consumer

StepConsumers: TypeAlias = list["aws_sdk_deadline.types.step_consumer.StepConsumer"]


# --- restJson1 ser/de ---
def serialize_json(value: StepConsumers) -> list:
    import aws_sdk_deadline.types.step_consumer

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.step_consumer.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepConsumers:
    import aws_sdk_deadline.types.step_consumer

    out: StepConsumers = []
    for item in data:
        out.append(aws_sdk_deadline.types.step_consumer.deserialize_json(item))
    return out
