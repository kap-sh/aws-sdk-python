"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobObjective``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_job_objective_type
    import capo_sagemaker.types.metric_name


class HyperParameterTuningJobObjective(TypedDict, closed=True):
    type: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_objective_type.HyperParameterTuningJobObjectiveType"
    ]
    """<p>Whether to minimize or maximize the objective metric.</p>"""
    metric_name: NotRequired["capo_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the metric to use for the objective metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobObjective) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_objective_type

        out["Type"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_objective_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobObjective:
    out: HyperParameterTuningJobObjective = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_sagemaker.types.hyper_parameter_tuning_job_objective_type

        out["type"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_objective_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    return out
