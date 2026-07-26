"""Generated from Smithy shape ``com.amazonaws.connect#CustomerQualityMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.audio_quality_metrics_info


class CustomerQualityMetrics(TypedDict, closed=True):
    audio: NotRequired[
        "capo_connect.types.audio_quality_metrics_info.AudioQualityMetricsInfo"
    ]
    """<p>Information about the audio quality of the Customer</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerQualityMetrics) -> dict:
    out: dict = {}
    if "audio" in value:
        import capo_connect.types.audio_quality_metrics_info

        out["Audio"] = capo_connect.types.audio_quality_metrics_info.serialize_json(
            value["audio"]
        )
    return out


def deserialize_json(data: dict) -> CustomerQualityMetrics:
    out: CustomerQualityMetrics = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import capo_connect.types.audio_quality_metrics_info

        out["audio"] = capo_connect.types.audio_quality_metrics_info.deserialize_json(
            data["Audio"]
        )
    return out
