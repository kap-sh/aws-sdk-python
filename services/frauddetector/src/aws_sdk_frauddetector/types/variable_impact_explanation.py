"""Generated from Smithy shape ``com.amazonaws.frauddetector#VariableImpactExplanation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float
    import aws_sdk_frauddetector.types.string


class VariableImpactExplanation(TypedDict):
    event_variable_name: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> The event variable name. </p>"""
    relative_impact: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> The event variable's relative impact in terms of magnitude on the prediction scores. The relative impact values consist of a numerical rating (0-5, 5 being the highest) and direction (increased/decreased) impact of the fraud risk. </p>"""
    log_odds_impact: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The raw, uninterpreted value represented as log-odds of the fraud. These values are usually between -10 to +10, but range from - infinity to + infinity.</p> <ul> <li> <p>A positive value indicates that the variable drove the risk score up.</p> </li> <li> <p>A negative value indicates that the variable drove the risk score down.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariableImpactExplanation) -> dict:
    out: dict = {}
    if "event_variable_name" in value:
        out["eventVariableName"] = value["event_variable_name"]
    if "relative_impact" in value:
        out["relativeImpact"] = value["relative_impact"]
    if "log_odds_impact" in value:
        out["logOddsImpact"] = value["log_odds_impact"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VariableImpactExplanation:
    out: VariableImpactExplanation = {}  # type: ignore[typeddict-item]
    if "eventVariableName" in data:
        out["event_variable_name"] = data["eventVariableName"]
    if "relativeImpact" in data:
        out["relative_impact"] = data["relativeImpact"]
    if "logOddsImpact" in data:
        out["log_odds_impact"] = data["logOddsImpact"]
    return out
