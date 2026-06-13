"""Generated from Smithy shape ``com.amazonaws.taxsettings#ValidationExceptionErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

ValidationExceptionErrorCode: TypeAlias = Literal[
    "MalformedToken",
    "ExpiredToken",
    "InvalidToken",
    "FieldValidationFailed",
    "MissingInput",
    "NonIndiaCustomerCanNotSetPAN",
    "GSTExistenceBlockSetPAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MalformedToken",
        "ExpiredToken",
        "InvalidToken",
        "FieldValidationFailed",
        "MissingInput",
        "NonIndiaCustomerCanNotSetPAN",
        "GSTExistenceBlockSetPAN",
    )
)


def serialize_json(value: ValidationExceptionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ValidationExceptionErrorCode value: {data!r}"
        )
    return cast(ValidationExceptionErrorCode, data)
