"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_primary_status
    import aws_sdk_sagemaker.types.trial_component_status_message


class TrialComponentStatus(TypedDict):
    primary_status: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_primary_status.TrialComponentPrimaryStatus"
    ]
    """<p>The status of the trial component.</p>"""
    message: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_status_message.TrialComponentStatusMessage"
    ]
    """<p>If the component failed, a message describing why.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentStatus) -> dict:
    out: dict = {}
    if "primary_status" in value:
        import aws_sdk_sagemaker.types.trial_component_primary_status

        out["PrimaryStatus"] = (
            aws_sdk_sagemaker.types.trial_component_primary_status.serialize_aws_json_1_1(
                value["primary_status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentStatus:
    out: TrialComponentStatus = {}  # type: ignore[typeddict-item]
    if "PrimaryStatus" in data:
        import aws_sdk_sagemaker.types.trial_component_primary_status

        out["primary_status"] = (
            aws_sdk_sagemaker.types.trial_component_primary_status.deserialize_aws_json_1_1(
                data["PrimaryStatus"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
