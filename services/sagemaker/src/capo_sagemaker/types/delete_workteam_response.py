"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteWorkteamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.success


class DeleteWorkteamResponse(TypedDict, closed=True):
    success: NotRequired["capo_sagemaker.types.success.Success"]
    """<p>Returns <code>true</code> if the work team was successfully deleted; otherwise, returns <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkteamResponse) -> dict:
    out: dict = {}
    if "success" in value:
        out["Success"] = value["success"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkteamResponse:
    out: DeleteWorkteamResponse = {}  # type: ignore[typeddict-item]
    if "Success" in data:
        out["success"] = data["Success"]
    return out
