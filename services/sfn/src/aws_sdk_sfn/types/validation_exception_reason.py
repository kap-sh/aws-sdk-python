"""Generated from Smithy shape ``com.amazonaws.sfn#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "API_DOES_NOT_SUPPORT_LABELED_ARNS",
    "MISSING_REQUIRED_PARAMETER",
    "CANNOT_UPDATE_COMPLETED_MAP_RUN",
    "INVALID_ROUTING_CONFIGURATION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API_DOES_NOT_SUPPORT_LABELED_ARNS",
        "MISSING_REQUIRED_PARAMETER",
        "CANNOT_UPDATE_COMPLETED_MAP_RUN",
        "INVALID_ROUTING_CONFIGURATION",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
