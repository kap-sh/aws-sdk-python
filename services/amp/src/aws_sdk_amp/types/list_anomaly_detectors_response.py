"""Generated from Smithy shape ``com.amazonaws.amp#ListAnomalyDetectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.anomaly_detector_summary_list
    import aws_sdk_amp.types.pagination_token


class ListAnomalyDetectorsResponse(TypedDict):
    anomaly_detectors: (
        "aws_sdk_amp.types.anomaly_detector_summary_list.AnomalyDetectorSummaryList"
    )
    """<p>The list of anomaly detectors in the workspace.</p>"""
    next_token: NotRequired["aws_sdk_amp.types.pagination_token.PaginationToken"]
    """<p>The pagination token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomalyDetectorsResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.anomaly_detector_summary_list

    out["anomalyDetectors"] = (
        aws_sdk_amp.types.anomaly_detector_summary_list.serialize_json(
            value["anomaly_detectors"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnomalyDetectorsResponse:
    out: ListAnomalyDetectorsResponse = {}  # type: ignore[typeddict-item]
    if "anomalyDetectors" in data:
        import aws_sdk_amp.types.anomaly_detector_summary_list

        out["anomaly_detectors"] = (
            aws_sdk_amp.types.anomaly_detector_summary_list.deserialize_json(
                data["anomalyDetectors"]
            )
        )
    else:
        raise DeserializationError(
            "ListAnomalyDetectorsResponse.anomaly_detectors required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
