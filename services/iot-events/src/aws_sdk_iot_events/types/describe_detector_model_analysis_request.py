"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeDetectorModelAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.analysis_id


class DescribeDetectorModelAnalysisRequest(TypedDict, closed=True):
    analysis_id: "aws_sdk_iot_events.types.analysis_id.AnalysisId"
    """<p>The ID of the analysis result that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorModelAnalysisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDetectorModelAnalysisRequest:
    out: DescribeDetectorModelAnalysisRequest = {}  # type: ignore[typeddict-item]
    return out
