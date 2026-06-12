"""Generated from Smithy shape ``com.amazonaws.transcribe#OutputLocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

OutputLocationType: TypeAlias = Literal[
    "CUSTOMER_BUCKET",
    "SERVICE_BUCKET",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_BUCKET",
        "SERVICE_BUCKET",
    )
)


def serialize_aws_json_1_1(value: OutputLocationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputLocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputLocationType value: {data!r}")
    return cast(OutputLocationType, data)
