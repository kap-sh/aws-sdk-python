"""Generated from Smithy shape ``com.amazonaws.kafka#UserIdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The identity type of the requester that calls the API operation.</p>"""
UserIdentityType: TypeAlias = Literal[
    "AWSACCOUNT",
    "AWSSERVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWSACCOUNT",
        "AWSSERVICE",
    )
)


def serialize_json(value: UserIdentityType) -> str:
    return value


def deserialize_json(data: str) -> UserIdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserIdentityType value: {data!r}")
    return cast(UserIdentityType, data)
