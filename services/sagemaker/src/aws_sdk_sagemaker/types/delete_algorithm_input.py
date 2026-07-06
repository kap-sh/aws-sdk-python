"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAlgorithmInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DeleteAlgorithmInput(TypedDict, closed=True):
    algorithm_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the algorithm to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAlgorithmInput) -> dict:
    out: dict = {}
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAlgorithmInput:
    out: DeleteAlgorithmInput = {}  # type: ignore[typeddict-item]
    if "AlgorithmName" in data:
        out["algorithm_name"] = data["AlgorithmName"]
    return out
