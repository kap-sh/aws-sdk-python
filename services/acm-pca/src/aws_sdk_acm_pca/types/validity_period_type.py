"""Generated from Smithy shape ``com.amazonaws.acmpca#ValidityPeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

ValidityPeriodType: TypeAlias = Literal[
    "END_DATE",
    "ABSOLUTE",
    "DAYS",
    "MONTHS",
    "YEARS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "END_DATE",
        "ABSOLUTE",
        "DAYS",
        "MONTHS",
        "YEARS",
    )
)


def serialize_aws_json_1_1(value: ValidityPeriodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidityPeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidityPeriodType value: {data!r}")
    return cast(ValidityPeriodType, data)
