"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudRiskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.known_fraudster_risk
    import aws_sdk_voice_id.types.voice_spoofing_risk


class FraudRiskDetails(TypedDict, closed=True):
    known_fraudster_risk: (
        "aws_sdk_voice_id.types.known_fraudster_risk.KnownFraudsterRisk"
    )
    """<p>The details resulting from 'Known Fraudster Risk' analysis of the speaker.</p>"""
    voice_spoofing_risk: "aws_sdk_voice_id.types.voice_spoofing_risk.VoiceSpoofingRisk"
    """<p>The details resulting from 'Voice Spoofing Risk' analysis of the speaker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudRiskDetails) -> dict:
    out: dict = {}
    import aws_sdk_voice_id.types.known_fraudster_risk

    out["KnownFraudsterRisk"] = (
        aws_sdk_voice_id.types.known_fraudster_risk.serialize_aws_json_1_0(
            value["known_fraudster_risk"]
        )
    )
    import aws_sdk_voice_id.types.voice_spoofing_risk

    out["VoiceSpoofingRisk"] = (
        aws_sdk_voice_id.types.voice_spoofing_risk.serialize_aws_json_1_0(
            value["voice_spoofing_risk"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> FraudRiskDetails:
    out: FraudRiskDetails = {}  # type: ignore[typeddict-item]
    if "KnownFraudsterRisk" in data:
        import aws_sdk_voice_id.types.known_fraudster_risk

        out["known_fraudster_risk"] = (
            aws_sdk_voice_id.types.known_fraudster_risk.deserialize_aws_json_1_0(
                data["KnownFraudsterRisk"]
            )
        )
    else:
        raise DeserializationError("FraudRiskDetails.known_fraudster_risk required")
    if "VoiceSpoofingRisk" in data:
        import aws_sdk_voice_id.types.voice_spoofing_risk

        out["voice_spoofing_risk"] = (
            aws_sdk_voice_id.types.voice_spoofing_risk.deserialize_aws_json_1_0(
                data["VoiceSpoofingRisk"]
            )
        )
    else:
        raise DeserializationError("FraudRiskDetails.voice_spoofing_risk required")
    return out
