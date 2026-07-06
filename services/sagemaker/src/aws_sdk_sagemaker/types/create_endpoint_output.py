"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_arn


class CreateEndpointOutput(TypedDict, closed=True):
    endpoint_arn: NotRequired["aws_sdk_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointOutput) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointOutput:
    out: CreateEndpointOutput = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    return out
