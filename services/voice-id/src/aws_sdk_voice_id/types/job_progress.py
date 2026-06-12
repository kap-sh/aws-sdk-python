"""Generated from Smithy shape ``com.amazonaws.voiceid#JobProgress``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.score


class JobProgress(TypedDict):
    percent_complete: NotRequired["aws_sdk_voice_id.types.score.Score"]
    """<p>Shows the completed percentage of enrollment or registration requests listed in the input file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobProgress) -> dict:
    out: dict = {}
    if "percent_complete" in value:
        out["PercentComplete"] = value["percent_complete"]
    return out


def deserialize_aws_json_1_0(data: dict) -> JobProgress:
    out: JobProgress = {}  # type: ignore[typeddict-item]
    if "PercentComplete" in data:
        out["percent_complete"] = data["PercentComplete"]
    return out
