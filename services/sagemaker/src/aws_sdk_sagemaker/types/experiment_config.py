"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExperimentConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name


class ExperimentConfig(TypedDict):
    experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of an existing experiment to associate with the trial component.</p>"""
    trial_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of an existing trial to associate the trial component with. If not specified, a new trial is created.</p>"""
    trial_component_display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The display name for the trial component. If this key isn't specified, the display name is the trial component name.</p>"""
    run_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment run to associate with the trial component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperimentConfig) -> dict:
    out: dict = {}
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "trial_component_display_name" in value:
        out["TrialComponentDisplayName"] = value["trial_component_display_name"]
    if "run_name" in value:
        out["RunName"] = value["run_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperimentConfig:
    out: ExperimentConfig = {}  # type: ignore[typeddict-item]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "TrialComponentDisplayName" in data:
        out["trial_component_display_name"] = data["TrialComponentDisplayName"]
    if "RunName" in data:
        out["run_name"] = data["RunName"]
    return out
