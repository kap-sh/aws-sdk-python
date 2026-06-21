"""Generated from Smithy shape ``com.amazonaws.dsql#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason for the validation exception.</p>"""
ValidationExceptionReason: TypeAlias = Literal[
    "unknownOperation",
    "cannotParse",
    "fieldValidationFailed",
    "deletionProtectionEnabled",
    "other",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
