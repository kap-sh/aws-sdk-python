"""Generated from Smithy shape ``com.amazonaws.fms#OrganizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

OrganizationStatus: TypeAlias = Literal[
    "ONBOARDING",
    "ONBOARDING_COMPLETE",
    "OFFBOARDING",
    "OFFBOARDING_COMPLETE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONBOARDING",
        "ONBOARDING_COMPLETE",
        "OFFBOARDING",
        "OFFBOARDING_COMPLETE",
    )
)


def serialize_aws_json_1_1(value: OrganizationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrganizationStatus value: {data!r}")
    return cast(OrganizationStatus, data)
