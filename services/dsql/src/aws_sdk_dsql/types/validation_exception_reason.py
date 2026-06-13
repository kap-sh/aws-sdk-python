"""Generated from Smithy shape ``com.amazonaws.dsql#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dsql.errors import DeserializationError

"""<p>The reason for the validation exception.</p>"""
ValidationExceptionReason: TypeAlias = Literal[
    "unknownOperation",
    "cannotParse",
    "fieldValidationFailed",
    "deletionProtectionEnabled",
    "other",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unknownOperation",
        "cannotParse",
        "fieldValidationFailed",
        "deletionProtectionEnabled",
        "other",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
