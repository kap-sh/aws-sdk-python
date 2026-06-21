"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

LicenseRecommendationFilterName: TypeAlias = Literal[
    "Finding",
    "FindingReasonCode",
    "LicenseName",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseRecommendationFilterName:
    return cast(LicenseRecommendationFilterName, data)
