"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateWorkteamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.workteam_arn


class CreateWorkteamResponse(TypedDict, closed=True):
    workteam_arn: NotRequired["capo_sagemaker.types.workteam_arn.WorkteamArn"]
    """<p>The Amazon Resource Name (ARN) of the work team. You can use this ARN to identify the work team.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkteamResponse) -> dict:
    out: dict = {}
    if "workteam_arn" in value:
        out["WorkteamArn"] = value["workteam_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkteamResponse:
    out: CreateWorkteamResponse = {}  # type: ignore[typeddict-item]
    if "WorkteamArn" in data:
        out["workteam_arn"] = data["WorkteamArn"]
    return out
