"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTrialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name


class UpdateTrialRequest(TypedDict, closed=True):
    trial_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial to update.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial as displayed. The name doesn't need to be unique. If <code>DisplayName</code> isn't specified, <code>TrialName</code> is displayed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrialRequest) -> dict:
    out: dict = {}
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrialRequest:
    out: UpdateTrialRequest = {}  # type: ignore[typeddict-item]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    return out
