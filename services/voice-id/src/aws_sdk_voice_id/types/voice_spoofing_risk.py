"""Generated from Smithy shape ``com.amazonaws.voiceid#VoiceSpoofingRisk``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.score


class VoiceSpoofingRisk(TypedDict, closed=True):
    risk_score: "aws_sdk_voice_id.types.score.Score"
    """<p>The score indicating the likelihood of speaker’s voice being spoofed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VoiceSpoofingRisk) -> dict:
    out: dict = {}
    out["RiskScore"] = value["risk_score"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VoiceSpoofingRisk:
    out: VoiceSpoofingRisk = {}  # type: ignore[typeddict-item]
    if "RiskScore" in data:
        out["risk_score"] = data["RiskScore"]
    else:
        raise DeserializationError("VoiceSpoofingRisk.risk_score required")
    return out
