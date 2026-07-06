"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_arn


class EndpointStepMetadata(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint in the step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointStepMetadata:
    out: EndpointStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
