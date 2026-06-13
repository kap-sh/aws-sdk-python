"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "unknownOperation",
    "cannotParse",
    "fieldValidationFailed",
    "invalidRequestFromMember",
    "disallowedRate",
    "other",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unknownOperation",
        "cannotParse",
        "fieldValidationFailed",
        "invalidRequestFromMember",
        "disallowedRate",
        "other",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
