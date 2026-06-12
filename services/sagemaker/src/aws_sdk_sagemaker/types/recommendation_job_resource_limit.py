"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobResourceLimit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_number_of_tests
    import aws_sdk_sagemaker.types.max_parallel_of_tests


class RecommendationJobResourceLimit(TypedDict):
    max_number_of_tests: NotRequired[
        "aws_sdk_sagemaker.types.max_number_of_tests.MaxNumberOfTests"
    ]
    """<p>Defines the maximum number of load tests.</p>"""
    max_parallel_of_tests: NotRequired[
        "aws_sdk_sagemaker.types.max_parallel_of_tests.MaxParallelOfTests"
    ]
    """<p>Defines the maximum number of parallel load tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobResourceLimit) -> dict:
    out: dict = {}
    if "max_number_of_tests" in value:
        out["MaxNumberOfTests"] = value["max_number_of_tests"]
    if "max_parallel_of_tests" in value:
        out["MaxParallelOfTests"] = value["max_parallel_of_tests"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobResourceLimit:
    out: RecommendationJobResourceLimit = {}  # type: ignore[typeddict-item]
    if "MaxNumberOfTests" in data:
        out["max_number_of_tests"] = data["MaxNumberOfTests"]
    if "MaxParallelOfTests" in data:
        out["max_parallel_of_tests"] = data["MaxParallelOfTests"]
    return out
