"""Generated from Smithy shape ``com.amazonaws.connect#AudioQualityMetricsInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.audio_quality_score
    import aws_sdk_connect.types.potential_audio_quality_issues


class AudioQualityMetricsInfo(TypedDict):
    quality_score: "aws_sdk_connect.types.audio_quality_score.AudioQualityScore"
    """<p>Number measuring the estimated quality of the media connection.</p>"""
    potential_quality_issues: NotRequired[
        "aws_sdk_connect.types.potential_audio_quality_issues.PotentialAudioQualityIssues"
    ]
    """<p>List of potential issues causing degradation of quality on a media connection. If the service did not detect any potential quality issues the list is empty.</p> <p>Valid values: <code>HighPacketLoss</code> | <code>HighRoundTripTime</code> | <code>HighJitterBuffer</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioQualityMetricsInfo) -> dict:
    out: dict = {}
    out["QualityScore"] = value.get("quality_score", 0)
    if "potential_quality_issues" in value:
        import aws_sdk_connect.types.potential_audio_quality_issues

        out["PotentialQualityIssues"] = (
            aws_sdk_connect.types.potential_audio_quality_issues.serialize_json(
                value["potential_quality_issues"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioQualityMetricsInfo:
    out: AudioQualityMetricsInfo = {}  # type: ignore[typeddict-item]
    if "QualityScore" in data:
        out["quality_score"] = data["QualityScore"]
    else:
        out["quality_score"] = 0
    if "PotentialQualityIssues" in data:
        import aws_sdk_connect.types.potential_audio_quality_issues

        out["potential_quality_issues"] = (
            aws_sdk_connect.types.potential_audio_quality_issues.deserialize_json(
                data["PotentialQualityIssues"]
            )
        )
    return out
