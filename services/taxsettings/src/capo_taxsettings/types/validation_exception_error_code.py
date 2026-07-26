"""Generated from Smithy shape ``com.amazonaws.taxsettings#ValidationExceptionErrorCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ValidationExceptionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionErrorCode:
    return cast(ValidationExceptionErrorCode, data)
