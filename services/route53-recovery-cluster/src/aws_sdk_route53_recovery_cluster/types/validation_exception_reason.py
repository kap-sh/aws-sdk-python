"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

"""Reason the request failed validation"""
ValidationExceptionReason: TypeAlias = Literal[
    "unknownOperation",
    "cannotParse",
    "fieldValidationFailed",
    "other",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
