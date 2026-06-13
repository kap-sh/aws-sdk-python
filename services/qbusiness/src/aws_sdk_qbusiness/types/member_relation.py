"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberRelation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

MemberRelation: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "OR",
    )
)


def serialize_json(value: MemberRelation) -> str:
    return value


def deserialize_json(data: str) -> MemberRelation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberRelation value: {data!r}")
    return cast(MemberRelation, data)
