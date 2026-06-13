"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_security.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "unknownOperation",
    "cannotParse",
    "fieldValidationFailed",
    "other",
    "lambdaCodeShaMisMatch",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unknownOperation",
        "cannotParse",
        "fieldValidationFailed",
        "other",
        "lambdaCodeShaMisMatch",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
