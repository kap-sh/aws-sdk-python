"""Generated from Smithy shape ``com.amazonaws.interconnect#RemoteAccountIdentifierType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_interconnect.errors import DeserializationError

RemoteAccountIdentifierType: TypeAlias = Literal[
    "account",
    "email",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "account",
        "email",
    )
)


def serialize_aws_json_1_0(value: RemoteAccountIdentifierType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RemoteAccountIdentifierType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RemoteAccountIdentifierType value: {data!r}"
        )
    return cast(RemoteAccountIdentifierType, data)
