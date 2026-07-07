"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTrialComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name


class DeleteTrialComponentRequest(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the component to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrialComponentRequest) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrialComponentRequest:
    out: DeleteTrialComponentRequest = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    return out
