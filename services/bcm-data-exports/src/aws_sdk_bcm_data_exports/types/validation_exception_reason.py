"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "unknownOperation",
    "cannotParse",
    "fieldValidationFailed",
    "other",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
