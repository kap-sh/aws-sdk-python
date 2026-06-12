"""Generated from Smithy shape ``com.amazonaws.lightsail#DnsRecordCreationStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

DnsRecordCreationStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "STARTED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "STARTED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: DnsRecordCreationStateCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DnsRecordCreationStateCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DnsRecordCreationStateCode value: {data!r}"
        )
    return cast(DnsRecordCreationStateCode, data)
