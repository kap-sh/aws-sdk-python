"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeSubscribedWorkteamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workteam_arn


class DescribeSubscribedWorkteamRequest(TypedDict, closed=True):
    workteam_arn: NotRequired["aws_sdk_sagemaker.types.workteam_arn.WorkteamArn"]
    """<p>The Amazon Resource Name (ARN) of the subscribed work team to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscribedWorkteamRequest) -> dict:
    out: dict = {}
    if "workteam_arn" in value:
        out["WorkteamArn"] = value["workteam_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscribedWorkteamRequest:
    out: DescribeSubscribedWorkteamRequest = {}  # type: ignore[typeddict-item]
    if "WorkteamArn" in data:
        out["workteam_arn"] = data["WorkteamArn"]
    return out
