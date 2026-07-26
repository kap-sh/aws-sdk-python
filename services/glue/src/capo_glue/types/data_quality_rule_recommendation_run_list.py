"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleRecommendationRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_recommendation_run_description

DataQualityRuleRecommendationRunList: TypeAlias = list[
    "capo_glue.types.data_quality_rule_recommendation_run_description.DataQualityRuleRecommendationRunDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleRecommendationRunList) -> list:
    import capo_glue.types.data_quality_rule_recommendation_run_description

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_rule_recommendation_run_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityRuleRecommendationRunList:
    import capo_glue.types.data_quality_rule_recommendation_run_description

    out: DataQualityRuleRecommendationRunList = []
    for item in data:
        out.append(
            capo_glue.types.data_quality_rule_recommendation_run_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
