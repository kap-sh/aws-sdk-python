"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationExportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.recommendation_export_job

RecommendationExportJobs: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.recommendation_export_job.RecommendationExportJob"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationExportJobs) -> list:
    import aws_sdk_compute_optimizer.types.recommendation_export_job

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_export_job.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationExportJobs:
    import aws_sdk_compute_optimizer.types.recommendation_export_job

    out: RecommendationExportJobs = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_export_job.deserialize_aws_json_1_0(
                item
            )
        )
    return out
