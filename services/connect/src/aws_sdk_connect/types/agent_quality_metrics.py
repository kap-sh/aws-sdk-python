"""Generated from Smithy shape ``com.amazonaws.connect#AgentQualityMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.audio_quality_metrics_info


class AgentQualityMetrics(TypedDict):
    audio: NotRequired[
        "aws_sdk_connect.types.audio_quality_metrics_info.AudioQualityMetricsInfo"
    ]
    """<p>Information about the audio quality of the Agent</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentQualityMetrics) -> dict:
    out: dict = {}
    if "audio" in value:
        import aws_sdk_connect.types.audio_quality_metrics_info

        out["Audio"] = aws_sdk_connect.types.audio_quality_metrics_info.serialize_json(
            value["audio"]
        )
    return out


def deserialize_json(data: dict) -> AgentQualityMetrics:
    out: AgentQualityMetrics = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import aws_sdk_connect.types.audio_quality_metrics_info

        out["audio"] = (
            aws_sdk_connect.types.audio_quality_metrics_info.deserialize_json(
                data["Audio"]
            )
        )
    return out
