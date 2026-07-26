"""Generated from Smithy shape ``com.amazonaws.connect#AgentQualityMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.audio_quality_metrics_info


class AgentQualityMetrics(TypedDict, closed=True):
    audio: NotRequired[
        "capo_connect.types.audio_quality_metrics_info.AudioQualityMetricsInfo"
    ]
    """<p>Information about the audio quality of the Agent</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentQualityMetrics) -> dict:
    out: dict = {}
    if "audio" in value:
        import capo_connect.types.audio_quality_metrics_info

        out["Audio"] = capo_connect.types.audio_quality_metrics_info.serialize_json(
            value["audio"]
        )
    return out


def deserialize_json(data: dict) -> AgentQualityMetrics:
    out: AgentQualityMetrics = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import capo_connect.types.audio_quality_metrics_info

        out["audio"] = capo_connect.types.audio_quality_metrics_info.deserialize_json(
            data["Audio"]
        )
    return out
