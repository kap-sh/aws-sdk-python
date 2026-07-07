"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrialComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name_or_arn


class DescribeTrialComponentRequest(TypedDict, closed=True):
    trial_component_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name_or_arn.ExperimentEntityNameOrArn"
    ]
    """<p>The name of the trial component to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrialComponentRequest) -> dict:
    out: dict = {}
    if "trial_component_name" in value:
        out["TrialComponentName"] = value["trial_component_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrialComponentRequest:
    out: DescribeTrialComponentRequest = {}  # type: ignore[typeddict-item]
    if "TrialComponentName" in data:
        out["trial_component_name"] = data["TrialComponentName"]
    return out
