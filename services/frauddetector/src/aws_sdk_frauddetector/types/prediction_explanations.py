"""Generated from Smithy shape ``com.amazonaws.frauddetector#PredictionExplanations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.list_of_aggregated_variables_impact_explanations
    import aws_sdk_frauddetector.types.list_of_variable_impact_explanations


class PredictionExplanations(TypedDict):
    variable_impact_explanations: NotRequired[
        "aws_sdk_frauddetector.types.list_of_variable_impact_explanations.listOfVariableImpactExplanations"
    ]
    """<p> The details of the event variable's impact on the prediction score. </p>"""
    aggregated_variables_impact_explanations: NotRequired[
        "aws_sdk_frauddetector.types.list_of_aggregated_variables_impact_explanations.ListOfAggregatedVariablesImpactExplanations"
    ]
    """<p> The details of the aggregated variables impact on the prediction score. </p> <p>Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are <code>IP address</code> and <code>user</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictionExplanations) -> dict:
    out: dict = {}
    if "variable_impact_explanations" in value:
        import aws_sdk_frauddetector.types.list_of_variable_impact_explanations

        out["variableImpactExplanations"] = (
            aws_sdk_frauddetector.types.list_of_variable_impact_explanations.serialize_aws_json_1_1(
                value["variable_impact_explanations"]
            )
        )
    if "aggregated_variables_impact_explanations" in value:
        import aws_sdk_frauddetector.types.list_of_aggregated_variables_impact_explanations

        out["aggregatedVariablesImpactExplanations"] = (
            aws_sdk_frauddetector.types.list_of_aggregated_variables_impact_explanations.serialize_aws_json_1_1(
                value["aggregated_variables_impact_explanations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictionExplanations:
    out: PredictionExplanations = {}  # type: ignore[typeddict-item]
    if "variableImpactExplanations" in data:
        import aws_sdk_frauddetector.types.list_of_variable_impact_explanations

        out["variable_impact_explanations"] = (
            aws_sdk_frauddetector.types.list_of_variable_impact_explanations.deserialize_aws_json_1_1(
                data["variableImpactExplanations"]
            )
        )
    if "aggregatedVariablesImpactExplanations" in data:
        import aws_sdk_frauddetector.types.list_of_aggregated_variables_impact_explanations

        out["aggregated_variables_impact_explanations"] = (
            aws_sdk_frauddetector.types.list_of_aggregated_variables_impact_explanations.deserialize_aws_json_1_1(
                data["aggregatedVariablesImpactExplanations"]
            )
        )
    return out
