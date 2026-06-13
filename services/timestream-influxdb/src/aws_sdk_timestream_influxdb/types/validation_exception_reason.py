"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "FIELD_VALIDATION_FAILED",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIELD_VALIDATION_FAILED",
        "OTHER",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
