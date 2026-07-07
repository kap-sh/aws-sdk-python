"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteWorkteamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workteam_name


class DeleteWorkteamRequest(TypedDict, closed=True):
    workteam_name: NotRequired["aws_sdk_sagemaker.types.workteam_name.WorkteamName"]
    """<p>The name of the work team to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkteamRequest) -> dict:
    out: dict = {}
    if "workteam_name" in value:
        out["WorkteamName"] = value["workteam_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkteamRequest:
    out: DeleteWorkteamRequest = {}  # type: ignore[typeddict-item]
    if "WorkteamName" in data:
        out["workteam_name"] = data["WorkteamName"]
    return out
