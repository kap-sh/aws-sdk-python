"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEndpointConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_config_arn


class CreateEndpointConfigOutput(TypedDict, closed=True):
    endpoint_config_arn: NotRequired[
        "capo_sagemaker.types.endpoint_config_arn.EndpointConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointConfigOutput) -> dict:
    out: dict = {}
    if "endpoint_config_arn" in value:
        out["EndpointConfigArn"] = value["endpoint_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointConfigOutput:
    out: CreateEndpointConfigOutput = {}  # type: ignore[typeddict-item]
    if "EndpointConfigArn" in data:
        out["endpoint_config_arn"] = data["EndpointConfigArn"]
    return out
