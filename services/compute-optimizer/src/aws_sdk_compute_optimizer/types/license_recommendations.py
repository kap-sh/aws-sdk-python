"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.license_recommendation

LicenseRecommendations: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.license_recommendation.LicenseRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendations) -> list:
    import aws_sdk_compute_optimizer.types.license_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.license_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseRecommendations:
    import aws_sdk_compute_optimizer.types.license_recommendation

    out: LicenseRecommendations = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.license_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
