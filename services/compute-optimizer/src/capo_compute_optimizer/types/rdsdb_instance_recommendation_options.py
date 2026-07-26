"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBInstanceRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rdsdb_instance_recommendation_option

RDSDBInstanceRecommendationOptions: TypeAlias = list[
    "capo_compute_optimizer.types.rdsdb_instance_recommendation_option.RDSDBInstanceRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBInstanceRecommendationOptions) -> list:
    import capo_compute_optimizer.types.rdsdb_instance_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.rdsdb_instance_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSDBInstanceRecommendationOptions:
    import capo_compute_optimizer.types.rdsdb_instance_recommendation_option

    out: RDSDBInstanceRecommendationOptions = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.rdsdb_instance_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
