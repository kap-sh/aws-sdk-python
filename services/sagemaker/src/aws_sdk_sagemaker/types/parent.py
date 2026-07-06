"""Generated from Smithy shape ``com.amazonaws.sagemaker#Parent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name


class Parent(TypedDict, closed=True):
    trial_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial.</p>"""
    experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the experiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parent) -> dict:
    out: dict = {}
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "experiment_name" in value:
        out["ExperimentName"] = value["experiment_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Parent:
    out: Parent = {}  # type: ignore[typeddict-item]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "ExperimentName" in data:
        out["experiment_name"] = data["ExperimentName"]
    return out
