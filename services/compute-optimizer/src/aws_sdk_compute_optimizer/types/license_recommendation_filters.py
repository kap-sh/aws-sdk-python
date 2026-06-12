"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.license_recommendation_filter

LicenseRecommendationFilters: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.license_recommendation_filter.LicenseRecommendationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendationFilters) -> list:
    import aws_sdk_compute_optimizer.types.license_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.license_recommendation_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseRecommendationFilters:
    import aws_sdk_compute_optimizer.types.license_recommendation_filter

    out: LicenseRecommendationFilters = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.license_recommendation_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
