"""Generated from Smithy shape ``com.amazonaws.lambda#Topics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.topic

Topics: TypeAlias = list["capo_lambda.types.topic.Topic"]


# --- restJson1 ser/de ---
def serialize_json(value: Topics) -> list:
    return list(value)


def deserialize_json(data: list) -> Topics:
    return list(data)
