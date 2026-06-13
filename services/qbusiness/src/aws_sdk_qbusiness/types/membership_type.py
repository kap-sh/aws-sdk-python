"""Generated from Smithy shape ``com.amazonaws.qbusiness#MembershipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

MembershipType: TypeAlias = Literal[
    "INDEX",
    "DATASOURCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INDEX",
        "DATASOURCE",
    )
)


def serialize_json(value: MembershipType) -> str:
    return value


def deserialize_json(data: str) -> MembershipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MembershipType value: {data!r}")
    return cast(MembershipType, data)
