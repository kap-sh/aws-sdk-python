"""Generated from Smithy shape ``com.amazonaws.licensemanager#RenewType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

RenewType: TypeAlias = Literal[
    "None",
    "Weekly",
    "Monthly",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Weekly",
        "Monthly",
    )
)


def serialize_aws_json_1_1(value: RenewType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RenewType value: {data!r}")
    return cast(RenewType, data)
