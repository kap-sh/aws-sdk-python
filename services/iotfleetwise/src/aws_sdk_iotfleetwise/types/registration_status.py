"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

RegistrationStatus: TypeAlias = Literal[
    "REGISTRATION_PENDING",
    "REGISTRATION_SUCCESS",
    "REGISTRATION_FAILURE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTRATION_PENDING",
        "REGISTRATION_SUCCESS",
        "REGISTRATION_FAILURE",
    )
)


def serialize_aws_json_1_0(value: RegistrationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RegistrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistrationStatus value: {data!r}")
    return cast(RegistrationStatus, data)
