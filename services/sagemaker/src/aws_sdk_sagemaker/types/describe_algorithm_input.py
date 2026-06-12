"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAlgorithmInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.arn_or_name


class DescribeAlgorithmInput(TypedDict):
    algorithm_name: NotRequired["aws_sdk_sagemaker.types.arn_or_name.ArnOrName"]
    """<p>The name of the algorithm to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAlgorithmInput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAlgorithmInput:
    out: DescribeAlgorithmInput = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    return out
