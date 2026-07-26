"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#FieldValidationCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: FieldValidationCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FieldValidationCode:
    return cast(FieldValidationCode, data)
