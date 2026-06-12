"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.rdsdb_recommendation

RDSDBRecommendations: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.rdsdb_recommendation.RDSDBRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBRecommendations) -> list:
    import aws_sdk_compute_optimizer.types.rdsdb_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.rdsdb_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSDBRecommendations:
    import aws_sdk_compute_optimizer.types.rdsdb_recommendation

    out: RDSDBRecommendations = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.rdsdb_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
