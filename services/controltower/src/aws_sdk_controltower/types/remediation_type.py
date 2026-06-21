"""Generated from Smithy shape ``com.amazonaws.controltower#RemediationType``."""

from typing import Literal, TypeAlias, cast

RemediationType: TypeAlias = Literal["INHERITANCE_DRIFT",]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationType) -> str:
    return value


def deserialize_json(data: str) -> RemediationType:
    return cast(RemediationType, data)
