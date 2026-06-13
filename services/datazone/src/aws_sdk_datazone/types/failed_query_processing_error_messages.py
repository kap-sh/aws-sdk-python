"""Generated from Smithy shape ``com.amazonaws.datazone#FailedQueryProcessingErrorMessages``."""

from typing import TypeAlias

FailedQueryProcessingErrorMessages: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: FailedQueryProcessingErrorMessages) -> list:
    return list(value)


def deserialize_json(data: list) -> FailedQueryProcessingErrorMessages:
    return list(data)
