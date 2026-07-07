"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobConsumedResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.integer


class HyperParameterTuningJobConsumedResources(TypedDict, closed=True):
    runtime_in_seconds: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The wall clock runtime in seconds used by your hyperparameter tuning job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobConsumedResources) -> dict:
    out: dict = {}
    if "runtime_in_seconds" in value:
        out["RuntimeInSeconds"] = value["runtime_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobConsumedResources:
    out: HyperParameterTuningJobConsumedResources = {}  # type: ignore[typeddict-item]
    if "RuntimeInSeconds" in data:
        out["runtime_in_seconds"] = data["RuntimeInSeconds"]
    return out
