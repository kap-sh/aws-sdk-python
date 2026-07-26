"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CallLegType``."""

from typing import Literal, TypeAlias, cast

CallLegType: TypeAlias = Literal[
    "Caller",
    "Callee",
]


# --- restJson1 ser/de ---
def serialize_json(value: CallLegType) -> str:
    return value


def deserialize_json(data: str) -> CallLegType:
    return cast(CallLegType, data)
