"""Generated from Smithy shape ``com.amazonaws.mediatailor#TrafficShapingRetrievalWindow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer


class TrafficShapingRetrievalWindow(TypedDict):
    retrieval_window_duration_seconds: NotRequired[
        "aws_sdk_mediatailor.types.__integer.__integer"
    ]
    """<p>The amount of time, in seconds, that MediaTailor spreads prefetch requests to the ADS. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficShapingRetrievalWindow) -> dict:
    out: dict = {}
    if "retrieval_window_duration_seconds" in value:
        out["RetrievalWindowDurationSeconds"] = value[
            "retrieval_window_duration_seconds"
        ]
    return out


def deserialize_json(data: dict) -> TrafficShapingRetrievalWindow:
    out: TrafficShapingRetrievalWindow = {}  # type: ignore[typeddict-item]
    if "RetrievalWindowDurationSeconds" in data:
        out["retrieval_window_duration_seconds"] = data[
            "RetrievalWindowDurationSeconds"
        ]
    return out
