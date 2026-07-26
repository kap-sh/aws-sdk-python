"""Generated from Smithy shape ``com.amazonaws.iotevents#StartDetectorModelAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.analysis_id


class StartDetectorModelAnalysisResponse(TypedDict, closed=True):
    analysis_id: NotRequired["capo_iot_events.types.analysis_id.AnalysisId"]
    """<p>The ID that you can use to retrieve the analysis result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDetectorModelAnalysisResponse) -> dict:
    out: dict = {}
    if "analysis_id" in value:
        out["analysisId"] = value["analysis_id"]
    return out


def deserialize_json(data: dict) -> StartDetectorModelAnalysisResponse:
    out: StartDetectorModelAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "analysisId" in data:
        out["analysis_id"] = data["analysisId"]
    return out
