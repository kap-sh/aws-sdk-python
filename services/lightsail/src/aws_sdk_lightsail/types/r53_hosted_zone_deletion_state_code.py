"""Generated from Smithy shape ``com.amazonaws.lightsail#R53HostedZoneDeletionStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

R53HostedZoneDeletionStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "PENDING",
    "FAILED",
    "STARTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "PENDING",
        "FAILED",
        "STARTED",
    )
)


def serialize_aws_json_1_1(value: R53HostedZoneDeletionStateCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> R53HostedZoneDeletionStateCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown R53HostedZoneDeletionStateCode value: {data!r}"
        )
    return cast(R53HostedZoneDeletionStateCode, data)
