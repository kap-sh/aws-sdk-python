"""Generated from Smithy shape ``com.amazonaws.frauddetector#listOfVariableImpactExplanations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.variable_impact_explanation

listOfVariableImpactExplanations: TypeAlias = list[
    "aws_sdk_frauddetector.types.variable_impact_explanation.VariableImpactExplanation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: listOfVariableImpactExplanations) -> list:
    import aws_sdk_frauddetector.types.variable_impact_explanation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.variable_impact_explanation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> listOfVariableImpactExplanations:
    import aws_sdk_frauddetector.types.variable_impact_explanation

    out: listOfVariableImpactExplanations = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.variable_impact_explanation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
