"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingStoppingCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_max_runtime_in_seconds


class ProcessingStoppingCondition(TypedDict, closed=True):
    max_runtime_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.processing_max_runtime_in_seconds.ProcessingMaxRuntimeInSeconds"
    ]
    """<p>Specifies the maximum runtime in seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingStoppingCondition) -> dict:
    out: dict = {}
    if "max_runtime_in_seconds" in value:
        out["MaxRuntimeInSeconds"] = value["max_runtime_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingStoppingCondition:
    out: ProcessingStoppingCondition = {}  # type: ignore[typeddict-item]
    if "MaxRuntimeInSeconds" in data:
        out["max_runtime_in_seconds"] = data["MaxRuntimeInSeconds"]
    return out
