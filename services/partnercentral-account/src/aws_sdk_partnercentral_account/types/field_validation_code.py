"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#FieldValidationCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

FieldValidationCode: TypeAlias = Literal[
    "REQUIRED_FIELD_MISSING",
    "DUPLICATE_VALUE",
    "INVALID_VALUE",
    "INVALID_STRING_FORMAT",
    "TOO_MANY_VALUES",
    "ACTION_NOT_PERMITTED",
    "INVALID_ENUM_VALUE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED_FIELD_MISSING",
        "DUPLICATE_VALUE",
        "INVALID_VALUE",
        "INVALID_STRING_FORMAT",
        "TOO_MANY_VALUES",
        "ACTION_NOT_PERMITTED",
        "INVALID_ENUM_VALUE",
    )
)


def serialize_aws_json_1_0(value: FieldValidationCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FieldValidationCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldValidationCode value: {data!r}")
    return cast(FieldValidationCode, data)
