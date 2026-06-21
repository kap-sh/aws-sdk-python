"""Generated from Smithy shape ``com.amazonaws.detective#InvitationType``."""

from typing import Literal, TypeAlias, cast

InvitationType: TypeAlias = Literal[
    "INVITATION",
    "ORGANIZATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvitationType) -> str:
    return value


def deserialize_json(data: str) -> InvitationType:
    return cast(InvitationType, data)
