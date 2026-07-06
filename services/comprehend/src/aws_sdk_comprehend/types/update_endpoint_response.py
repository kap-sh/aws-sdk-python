"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_model_arn


class UpdateEndpointResponse(TypedDict, closed=True):
    desired_model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the new model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointResponse) -> dict:
    out: dict = {}
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointResponse:
    out: UpdateEndpointResponse = {}  # type: ignore[typeddict-item]
    if "DesiredModelArn" in data:
        out["desired_model_arn"] = data["DesiredModelArn"]
    return out
