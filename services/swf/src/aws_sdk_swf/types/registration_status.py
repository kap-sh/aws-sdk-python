"""Generated from Smithy shape ``com.amazonaws.swf#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

RegistrationStatus: TypeAlias = Literal[
    "REGISTERED",
    "DEPRECATED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTERED",
        "DEPRECATED",
    )
)


def serialize_aws_json_1_0(value: RegistrationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RegistrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistrationStatus value: {data!r}")
    return cast(RegistrationStatus, data)
