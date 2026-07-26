"""Generated from Smithy shape ``com.amazonaws.detective#MemberDisabledReason``."""

from typing import Literal, TypeAlias, cast

MemberDisabledReason: TypeAlias = Literal[
    "VOLUME_TOO_HIGH",
    "VOLUME_UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberDisabledReason) -> str:
    return value


def deserialize_json(data: str) -> MemberDisabledReason:
    return cast(MemberDisabledReason, data)
