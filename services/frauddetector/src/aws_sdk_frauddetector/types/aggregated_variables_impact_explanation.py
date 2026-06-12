"""Generated from Smithy shape ``com.amazonaws.frauddetector#AggregatedVariablesImpactExplanation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float
    import aws_sdk_frauddetector.types.list_of_strings
    import aws_sdk_frauddetector.types.string


class AggregatedVariablesImpactExplanation(TypedDict):
    event_variable_names: NotRequired[
        "aws_sdk_frauddetector.types.list_of_strings.ListOfStrings"
    ]
    """<p> The names of all the event variables that were used to derive the aggregated variables. </p>"""
    relative_impact: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> The relative impact of the aggregated variables in terms of magnitude on the prediction scores. </p>"""
    log_odds_impact: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The raw, uninterpreted value represented as log-odds of the fraud. These values are usually between -10 to +10, but range from -infinity to +infinity.</p> <ul> <li> <p>A positive value indicates that the variables drove the risk score up.</p> </li> <li> <p>A negative value indicates that the variables drove the risk score down.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedVariablesImpactExplanation) -> dict:
    out: dict = {}
    if "event_variable_names" in value:
        import aws_sdk_frauddetector.types.list_of_strings

        out["eventVariableNames"] = (
            aws_sdk_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["event_variable_names"]
            )
        )
    if "relative_impact" in value:
        out["relativeImpact"] = value["relative_impact"]
    if "log_odds_impact" in value:
        out["logOddsImpact"] = value["log_odds_impact"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatedVariablesImpactExplanation:
    out: AggregatedVariablesImpactExplanation = {}  # type: ignore[typeddict-item]
    if "eventVariableNames" in data:
        import aws_sdk_frauddetector.types.list_of_strings

        out["event_variable_names"] = (
            aws_sdk_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["eventVariableNames"]
            )
        )
    if "relativeImpact" in data:
        out["relative_impact"] = data["relativeImpact"]
    if "logOddsImpact" in data:
        out["log_odds_impact"] = data["logOddsImpact"]
    return out
