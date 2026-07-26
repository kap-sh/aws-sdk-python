"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfLoggingStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.logging_strategy

__listOfLoggingStrategies: TypeAlias = list[
    "capo_mediatailor.types.logging_strategy.LoggingStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfLoggingStrategies) -> list:
    import capo_mediatailor.types.logging_strategy

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.logging_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfLoggingStrategies:
    import capo_mediatailor.types.logging_strategy

    out: __listOfLoggingStrategies = []
    for item in data:
        out.append(capo_mediatailor.types.logging_strategy.deserialize_json(item))
    return out
