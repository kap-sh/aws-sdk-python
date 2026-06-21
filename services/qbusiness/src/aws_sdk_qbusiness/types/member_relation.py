"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberRelation``."""

from typing import Literal, TypeAlias, cast

MemberRelation: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberRelation) -> str:
    return value


def deserialize_json(data: str) -> MemberRelation:
    return cast(MemberRelation, data)
