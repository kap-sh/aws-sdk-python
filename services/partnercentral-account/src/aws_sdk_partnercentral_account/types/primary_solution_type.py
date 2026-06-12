"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PrimarySolutionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

PrimarySolutionType: TypeAlias = Literal[
    "SOFTWARE_PRODUCTS",
    "CONSULTING_SERVICES",
    "PROFESSIONAL_SERVICES",
    "MANAGED_SERVICES",
    "HARDWARE_PRODUCTS",
    "COMMUNICATION_SERVICES",
    "VALUE_ADDED_RESALE_AWS_SERVICES",
    "TRAINING_SERVICES",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOFTWARE_PRODUCTS",
        "CONSULTING_SERVICES",
        "PROFESSIONAL_SERVICES",
        "MANAGED_SERVICES",
        "HARDWARE_PRODUCTS",
        "COMMUNICATION_SERVICES",
        "VALUE_ADDED_RESALE_AWS_SERVICES",
        "TRAINING_SERVICES",
    )
)


def serialize_aws_json_1_0(value: PrimarySolutionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PrimarySolutionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrimarySolutionType value: {data!r}")
    return cast(PrimarySolutionType, data)
