"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfLoggingStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.logging_strategy

__listOfLoggingStrategies: TypeAlias = list[
    "aws_sdk_mediatailor.types.logging_strategy.LoggingStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfLoggingStrategies) -> list:
    import aws_sdk_mediatailor.types.logging_strategy

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.logging_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfLoggingStrategies:
    import aws_sdk_mediatailor.types.logging_strategy

    out: __listOfLoggingStrategies = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.logging_strategy.deserialize_json(item))
    return out
