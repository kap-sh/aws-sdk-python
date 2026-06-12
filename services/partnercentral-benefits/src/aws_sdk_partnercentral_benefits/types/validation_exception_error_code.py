"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ValidationExceptionErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_benefits.errors import DeserializationError

ValidationExceptionErrorCode: TypeAlias = Literal[
    "REQUIRED_FIELD_MISSING",
    "INVALID_ENUM_VALUE",
    "INVALID_STRING_FORMAT",
    "INVALID_VALUE",
    "NOT_ENOUGH_VALUES",
    "TOO_MANY_VALUES",
    "INVALID_RESOURCE_STATE",
    "DUPLICATE_KEY_VALUE",
    "VALUE_OUT_OF_RANGE",
    "ACTION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED_FIELD_MISSING",
        "INVALID_ENUM_VALUE",
        "INVALID_STRING_FORMAT",
        "INVALID_VALUE",
        "NOT_ENOUGH_VALUES",
        "TOO_MANY_VALUES",
        "INVALID_RESOURCE_STATE",
        "DUPLICATE_KEY_VALUE",
        "VALUE_OUT_OF_RANGE",
        "ACTION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ValidationExceptionErrorCode value: {data!r}"
        )
    return cast(ValidationExceptionErrorCode, data)
