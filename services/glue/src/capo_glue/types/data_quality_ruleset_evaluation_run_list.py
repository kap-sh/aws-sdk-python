"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRulesetEvaluationRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_evaluation_run_description

DataQualityRulesetEvaluationRunList: TypeAlias = list[
    "capo_glue.types.data_quality_ruleset_evaluation_run_description.DataQualityRulesetEvaluationRunDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRulesetEvaluationRunList) -> list:
    import capo_glue.types.data_quality_ruleset_evaluation_run_description

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_ruleset_evaluation_run_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityRulesetEvaluationRunList:
    import capo_glue.types.data_quality_ruleset_evaluation_run_description

    out: DataQualityRulesetEvaluationRunList = []
    for item in data:
        out.append(
            capo_glue.types.data_quality_ruleset_evaluation_run_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
