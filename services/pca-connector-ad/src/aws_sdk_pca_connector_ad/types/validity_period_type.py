"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ValidityPeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

ValidityPeriodType: TypeAlias = Literal[
    "HOURS",
    "DAYS",
    "WEEKS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURS",
        "DAYS",
        "WEEKS",
        "MONTHS",
        "YEARS",
    )
)


def serialize_json(value: ValidityPeriodType) -> str:
    return value


def deserialize_json(data: str) -> ValidityPeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidityPeriodType value: {data!r}")
    return cast(ValidityPeriodType, data)
