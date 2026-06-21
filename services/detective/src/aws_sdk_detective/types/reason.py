"""Generated from Smithy shape ``com.amazonaws.detective#Reason``."""

from typing import Literal, TypeAlias, cast

Reason: TypeAlias = Literal["AWS_THREAT_INTELLIGENCE",]


# --- restJson1 ser/de ---
def serialize_json(value: Reason) -> str:
    return value


def deserialize_json(data: str) -> Reason:
    return cast(Reason, data)
