"""Generated from Smithy shape ``com.amazonaws.glue#PrincipalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

PrincipalType: TypeAlias = Literal[
    "USER",
    "ROLE",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "ROLE",
        "GROUP",
    )
)


def serialize_aws_json_1_1(value: PrincipalType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrincipalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalType value: {data!r}")
    return cast(PrincipalType, data)
