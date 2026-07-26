"""Generated from Smithy shape ``com.amazonaws.forecast#CreateExplainabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class CreateExplainabilityResponse(TypedDict, closed=True):
    explainability_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Explainability.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExplainabilityResponse) -> dict:
    out: dict = {}
    if "explainability_arn" in value:
        out["ExplainabilityArn"] = value["explainability_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExplainabilityResponse:
    out: CreateExplainabilityResponse = {}  # type: ignore[typeddict-item]
    if "ExplainabilityArn" in data:
        out["explainability_arn"] = data["ExplainabilityArn"]
    return out
