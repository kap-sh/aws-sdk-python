"""Generated from Smithy shape ``com.amazonaws.mpa#ActionCompletionStrategy``."""

from typing import Literal, TypeAlias, cast

ActionCompletionStrategy: TypeAlias = Literal["AUTO_COMPLETION_UPON_APPROVAL",]


# --- restJson1 ser/de ---
def serialize_json(value: ActionCompletionStrategy) -> str:
    return value


def deserialize_json(data: str) -> ActionCompletionStrategy:
    return cast(ActionCompletionStrategy, data)
