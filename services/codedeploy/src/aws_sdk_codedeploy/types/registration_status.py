"""Generated from Smithy shape ``com.amazonaws.codedeploy#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

RegistrationStatus: TypeAlias = Literal[
    "Registered",
    "Deregistered",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Registered",
        "Deregistered",
    )
)


def serialize_aws_json_1_1(value: RegistrationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegistrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistrationStatus value: {data!r}")
    return cast(RegistrationStatus, data)
