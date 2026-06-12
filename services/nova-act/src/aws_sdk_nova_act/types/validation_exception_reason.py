"""Generated from Smithy shape ``com.amazonaws.novaact#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_nova_act.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "FieldValidationFailed",
    "InvalidStatus",
    "GuardrailIntervened",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FieldValidationFailed",
        "InvalidStatus",
        "GuardrailIntervened",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
