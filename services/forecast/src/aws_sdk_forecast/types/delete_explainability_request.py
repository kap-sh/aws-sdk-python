"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteExplainabilityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DeleteExplainabilityRequest(TypedDict):
    explainability_arn: "aws_sdk_forecast.types.arn.Arn"
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
