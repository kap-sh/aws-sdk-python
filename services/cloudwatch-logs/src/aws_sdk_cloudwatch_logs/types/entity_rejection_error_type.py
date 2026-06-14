"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EntityRejectionErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

EntityRejectionErrorType: TypeAlias = Literal[
    "InvalidEntity",
    "InvalidTypeValue",
    "InvalidKeyAttributes",
    "InvalidAttributes",
    "EntitySizeTooLarge",
    "UnsupportedLogGroupType",
    "MissingRequiredFields",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidEntity",
        "InvalidTypeValue",
        "InvalidKeyAttributes",
        "InvalidAttributes",
        "EntitySizeTooLarge",
        "UnsupportedLogGroupType",
        "MissingRequiredFields",
    )
)


def serialize_aws_json_1_1(value: EntityRejectionErrorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityRejectionErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityRejectionErrorType value: {data!r}")
    return cast(EntityRejectionErrorType, data)
