"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeDetectorModelAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.analysis_status


class DescribeDetectorModelAnalysisResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_iot_events.types.analysis_status.AnalysisStatus"]
    """<p>The status of the analysis activity. The status can be one of the following values:</p> <ul> <li> <p> <code>RUNNING</code> - AWS IoT Events is analyzing your detector model. This process can take several minutes to complete.</p> </li> <li> <p> <code>COMPLETE</code> - AWS IoT Events finished analyzing your detector model.</p> </li> <li> <p> <code>FAILED</code> - AWS IoT Events couldn't analyze your detector model. Try again later.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectorModelAnalysisResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_iot_events.types.analysis_status

        out["status"] = aws_sdk_iot_events.types.analysis_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDetectorModelAnalysisResponse:
    out: DescribeDetectorModelAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_iot_events.types.analysis_status

        out["status"] = aws_sdk_iot_events.types.analysis_status.deserialize_json(
            data["status"]
        )
    return out
