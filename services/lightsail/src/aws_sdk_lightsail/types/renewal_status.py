"""Generated from Smithy shape ``com.amazonaws.lightsail#RenewalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

RenewalStatus: TypeAlias = Literal[
    "PendingAutoRenewal",
    "PendingValidation",
    "Success",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PendingAutoRenewal",
        "PendingValidation",
        "Success",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: RenewalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RenewalStatus value: {data!r}")
    return cast(RenewalStatus, data)
