"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfAggregatedVariablesImpactExplanations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.aggregated_variables_impact_explanation

ListOfAggregatedVariablesImpactExplanations: TypeAlias = list[
    "aws_sdk_frauddetector.types.aggregated_variables_impact_explanation.AggregatedVariablesImpactExplanation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfAggregatedVariablesImpactExplanations) -> list:
    import aws_sdk_frauddetector.types.aggregated_variables_impact_explanation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.aggregated_variables_impact_explanation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfAggregatedVariablesImpactExplanations:
    import aws_sdk_frauddetector.types.aggregated_variables_impact_explanation

    out: ListOfAggregatedVariablesImpactExplanations = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.aggregated_variables_impact_explanation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
