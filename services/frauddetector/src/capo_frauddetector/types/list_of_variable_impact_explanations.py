"""Generated from Smithy shape ``com.amazonaws.frauddetector#listOfVariableImpactExplanations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.variable_impact_explanation

listOfVariableImpactExplanations: TypeAlias = list[
    "capo_frauddetector.types.variable_impact_explanation.VariableImpactExplanation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: listOfVariableImpactExplanations) -> list:
    import capo_frauddetector.types.variable_impact_explanation

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.variable_impact_explanation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> listOfVariableImpactExplanations:
    import capo_frauddetector.types.variable_impact_explanation

    out: listOfVariableImpactExplanations = []
    for item in data:
        out.append(
            capo_frauddetector.types.variable_impact_explanation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
