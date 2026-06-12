"""Generated from Smithy shape ``com.amazonaws.transfer#EnforceMessageSigningType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

EnforceMessageSigningType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: EnforceMessageSigningType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnforceMessageSigningType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnforceMessageSigningType value: {data!r}")
    return cast(EnforceMessageSigningType, data)
