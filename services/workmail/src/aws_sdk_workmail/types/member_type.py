"""Generated from Smithy shape ``com.amazonaws.workmail#MemberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

MemberType: TypeAlias = Literal[
    "GROUP",
    "USER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GROUP",
        "USER",
    )
)


def serialize_aws_json_1_1(value: MemberType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MemberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberType value: {data!r}")
    return cast(MemberType, data)
