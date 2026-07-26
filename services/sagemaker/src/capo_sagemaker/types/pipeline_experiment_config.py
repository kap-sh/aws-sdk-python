"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineExperimentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name


class PipelineExperimentConfig(TypedDict, closed=True):
    experiment_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment.</p>"""
    trial_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExperimentConfig) -> dict:
    out: dict = {}
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExperimentConfig:
    out: PipelineExperimentConfig = {}  # type: ignore[typeddict-item]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    return out
