"""Generated from Smithy shape ``com.amazonaws.voiceid#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.s3_uri


class InputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_voice_id.types.s3_uri.S3Uri"
    """<p>The S3 location for the input manifest file that contains the list of individual enrollment or registration job requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("InputDataConfig.s3_uri required")
    return out
