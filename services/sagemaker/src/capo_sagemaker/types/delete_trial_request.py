"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTrialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name


class DeleteTrialRequest(TypedDict, closed=True):
    trial_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the trial to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrialRequest) -> dict:
    out: dict = {}
    if "trial_name" in value:
        out["TrialName"] = value["trial_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrialRequest:
    out: DeleteTrialRequest = {}  # type: ignore[typeddict-item]
    if "TrialName" in data:
        out["trial_name"] = data["TrialName"]
    return out
