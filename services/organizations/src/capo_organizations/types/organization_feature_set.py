"""Generated from Smithy shape ``com.amazonaws.organizations#OrganizationFeatureSet``."""

from typing import Literal, TypeAlias, cast

OrganizationFeatureSet: TypeAlias = Literal[
    "ALL",
    "CONSOLIDATED_BILLING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationFeatureSet) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationFeatureSet:
    return cast(OrganizationFeatureSet, data)
