"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringStoppingCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_max_runtime_in_seconds


class MonitoringStoppingCondition(TypedDict, closed=True):
    max_runtime_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_max_runtime_in_seconds.MonitoringMaxRuntimeInSeconds"
    ]
    """<p>The maximum runtime allowed in seconds.</p> <note> <p>The <code>MaxRuntimeInSeconds</code> cannot exceed the frequency of the job. For data quality and model explainability, this can be up to 3600 seconds for an hourly schedule. For model bias and model quality hourly schedules, this can be up to 1800 seconds.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringStoppingCondition) -> dict:
    out: dict = {}
    if "max_runtime_in_seconds" in value:
        out["MaxRuntimeInSeconds"] = value["max_runtime_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringStoppingCondition:
    out: MonitoringStoppingCondition = {}  # type: ignore[typeddict-item]
    if "MaxRuntimeInSeconds" in data:
        out["max_runtime_in_seconds"] = data["MaxRuntimeInSeconds"]
    return out
