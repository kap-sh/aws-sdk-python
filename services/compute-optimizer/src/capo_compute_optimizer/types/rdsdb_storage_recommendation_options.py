"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBStorageRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rdsdb_storage_recommendation_option

RDSDBStorageRecommendationOptions: TypeAlias = list[
    "capo_compute_optimizer.types.rdsdb_storage_recommendation_option.RDSDBStorageRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBStorageRecommendationOptions) -> list:
    import capo_compute_optimizer.types.rdsdb_storage_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.rdsdb_storage_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSDBStorageRecommendationOptions:
    import capo_compute_optimizer.types.rdsdb_storage_recommendation_option

    out: RDSDBStorageRecommendationOptions = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.rdsdb_storage_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
