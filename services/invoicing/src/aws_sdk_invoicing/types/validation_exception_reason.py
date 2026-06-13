"""Generated from Smithy shape ``com.amazonaws.invoicing#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "nonMemberPresent",
    "maxAccountsExceeded",
    "maxInvoiceUnitsExceeded",
    "duplicateInvoiceUnit",
    "mutualExclusionError",
    "accountMembershipError",
    "taxSettingsError",
    "expiredNextToken",
    "invalidNextToken",
    "invalidInput",
    "fieldValidationFailed",
    "cannotParse",
    "unknownOperation",
    "other",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "nonMemberPresent",
        "maxAccountsExceeded",
        "maxInvoiceUnitsExceeded",
        "duplicateInvoiceUnit",
        "mutualExclusionError",
        "accountMembershipError",
        "taxSettingsError",
        "expiredNextToken",
        "invalidNextToken",
        "invalidInput",
        "fieldValidationFailed",
        "cannotParse",
        "unknownOperation",
        "other",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
