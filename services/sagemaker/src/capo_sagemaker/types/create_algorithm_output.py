"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAlgorithmOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_arn


class CreateAlgorithmOutput(TypedDict, closed=True):
    algorithm_arn: NotRequired["capo_sagemaker.types.algorithm_arn.AlgorithmArn"]
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
