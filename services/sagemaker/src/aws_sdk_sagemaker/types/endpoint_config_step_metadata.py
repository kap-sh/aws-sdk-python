"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointConfigStepMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_config_arn


class EndpointConfigStepMetadata(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.endpoint_config_arn.EndpointConfigArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint configuration used in the step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointConfigStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointConfigStepMetadata:
    out: EndpointConfigStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
