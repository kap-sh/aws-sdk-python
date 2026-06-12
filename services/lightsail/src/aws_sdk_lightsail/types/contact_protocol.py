"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContactProtocol: TypeAlias = Literal[
    "Email",
    "SMS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Email",
        "SMS",
    )
)


def serialize_aws_json_1_1(value: ContactProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactProtocol value: {data!r}")
    return cast(ContactProtocol, data)
