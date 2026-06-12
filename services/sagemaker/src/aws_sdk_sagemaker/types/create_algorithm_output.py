"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAlgorithmOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_arn


class CreateAlgorithmOutput(TypedDict):
    algorithm_arn: NotRequired["aws_sdk_sagemaker.types.algorithm_arn.AlgorithmArn"]
    """<p>The Amazon Resource Name (ARN) of the new algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAlgorithmOutput) -> dict:
    out: dict = {}
    if "algorithm_arn" in value:
        out["AlgorithmArn"] = value["algorithm_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAlgorithmOutput:
    out: CreateAlgorithmOutput = {}  # type: ignore[typeddict-item]
    if "AlgorithmArn" in data:
        out["algorithm_arn"] = data["AlgorithmArn"]
    return out
