"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

CreateAccountState: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CreateAccountState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CreateAccountState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CreateAccountState value: {data!r}")
    return cast(CreateAccountState, data)
