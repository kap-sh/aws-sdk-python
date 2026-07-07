"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociateTrialComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name


class AssociateTrialComponentRequest(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component to associated with the trial.</p>"""
    trial_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial to associate with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateTrialComponentRequest) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateTrialComponentRequest:
    out: AssociateTrialComponentRequest = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    return out
