"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateWorkteamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.workteam


class UpdateWorkteamResponse(TypedDict, closed=True):
    workteam: NotRequired["capo_sagemaker.types.workteam.Workteam"]
    """<p>A <code>Workteam</code> object that describes the updated work team.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkteamResponse) -> dict:
    out: dict = {}
    if "workteam" in value:
        import capo_sagemaker.types.workteam

        out["Workteam"] = capo_sagemaker.types.workteam.serialize_aws_json_1_1(
            value["workteam"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkteamResponse:
    out: UpdateWorkteamResponse = {}  # type: ignore[typeddict-item]
    if "Workteam" in data:
        import capo_sagemaker.types.workteam

        out["workteam"] = capo_sagemaker.types.workteam.deserialize_aws_json_1_1(
            data["Workteam"]
        )
    return out
