"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteExplainabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DeleteExplainabilityRequest(TypedDict, closed=True):
    explainability_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Explainability resource to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExplainabilityRequest) -> dict:
    out: dict = {}
    out["ExplainabilityArn"] = value["explainability_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExplainabilityRequest:
    out: DeleteExplainabilityRequest = {}  # type: ignore[typeddict-item]
    if "ExplainabilityArn" in data:
        out["explainability_arn"] = data["ExplainabilityArn"]
    else:
        raise DeserializationError(
            "DeleteExplainabilityRequest.explainability_arn required"
        )
    return out
