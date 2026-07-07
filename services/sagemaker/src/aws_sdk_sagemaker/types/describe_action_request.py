"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name_or_arn


class DescribeActionRequest(TypedDict, closed=True):
    action_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name_or_arn.ExperimentEntityNameOrArn"
    ]
    """<p>The name of the action to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeActionRequest) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeActionRequest:
    out: DescribeActionRequest = {}  # type: ignore[typeddict-item]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    return out
