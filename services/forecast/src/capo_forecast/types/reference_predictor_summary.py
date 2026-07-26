"""Generated from Smithy shape ``com.amazonaws.forecast#ReferencePredictorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.state


class ReferencePredictorSummary(TypedDict, closed=True):
    arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The ARN of the reference predictor.</p>"""
    state: NotRequired["capo_forecast.types.state.State"]
    """<p>Whether the reference predictor is <code>Active</code> or <code>Deleted</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferencePredictorSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "state" in value:
        import capo_forecast.types.state

        out["State"] = capo_forecast.types.state.serialize_aws_json_1_1(value["state"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferencePredictorSummary:
    out: ReferencePredictorSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "State" in data:
        import capo_forecast.types.state

        out["state"] = capo_forecast.types.state.deserialize_aws_json_1_1(data["State"])
    return out
