"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateEndpointWeightsAndCapacitiesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_arn


class UpdateEndpointWeightsAndCapacitiesOutput(TypedDict):
    endpoint_arn: NotRequired["aws_sdk_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the updated endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointWeightsAndCapacitiesOutput) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointWeightsAndCapacitiesOutput:
    out: UpdateEndpointWeightsAndCapacitiesOutput = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    return out
