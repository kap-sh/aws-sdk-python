"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rdsdb_recommendation

RDSDBRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.rdsdb_recommendation.RDSDBRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBRecommendations) -> list:
    import capo_compute_optimizer.types.rdsdb_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.rdsdb_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSDBRecommendations:
    import capo_compute_optimizer.types.rdsdb_recommendation

    out: RDSDBRecommendations = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.rdsdb_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
