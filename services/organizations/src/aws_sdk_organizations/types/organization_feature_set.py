"""Generated from Smithy shape ``com.amazonaws.organizations#OrganizationFeatureSet``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

OrganizationFeatureSet: TypeAlias = Literal[
    "ALL",
    "CONSOLIDATED_BILLING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "CONSOLIDATED_BILLING",
    )
)


def serialize_aws_json_1_1(value: OrganizationFeatureSet) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationFeatureSet:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrganizationFeatureSet value: {data!r}")
    return cast(OrganizationFeatureSet, data)
