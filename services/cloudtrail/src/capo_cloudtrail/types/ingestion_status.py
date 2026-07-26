"""Generated from Smithy shape ``com.amazonaws.cloudtrail#IngestionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.error_message
    import capo_cloudtrail.types.uuid


class IngestionStatus(TypedDict, closed=True):
    latest_ingestion_success_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The time stamp of the most recent successful ingestion of events for the channel.</p>"""
    latest_ingestion_success_event_id: NotRequired["capo_cloudtrail.types.uuid.UUID"]
    """<p>The event ID of the most recent successful ingestion of events.</p>"""
    latest_ingestion_error_code: NotRequired[
        "capo_cloudtrail.types.error_message.ErrorMessage"
    ]
    """<p>The error code for the most recent failure to ingest events.</p>"""
    latest_ingestion_attempt_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The time stamp of the most recent attempt to ingest events on the channel.</p>"""
    latest_ingestion_attempt_event_id: NotRequired["capo_cloudtrail.types.uuid.UUID"]
    """<p>The event ID of the most recent attempt to ingest events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngestionStatus) -> dict:
    out: dict = {}
    if "latest_ingestion_success_time" in value:
        import capo_cloudtrail.types.date

        out["LatestIngestionSuccessTime"] = (
            capo_cloudtrail.types.date.serialize_aws_json_1_1(
                value["latest_ingestion_success_time"]
            )
        )
    if "latest_ingestion_success_event_id" in value:
        out["LatestIngestionSuccessEventID"] = value[
            "latest_ingestion_success_event_id"
        ]
    if "latest_ingestion_error_code" in value:
        out["LatestIngestionErrorCode"] = value["latest_ingestion_error_code"]
    if "latest_ingestion_attempt_time" in value:
        import capo_cloudtrail.types.date

        out["LatestIngestionAttemptTime"] = (
            capo_cloudtrail.types.date.serialize_aws_json_1_1(
                value["latest_ingestion_attempt_time"]
            )
        )
    if "latest_ingestion_attempt_event_id" in value:
        out["LatestIngestionAttemptEventID"] = value[
            "latest_ingestion_attempt_event_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> IngestionStatus:
    out: IngestionStatus = {}  # type: ignore[typeddict-item]
    if "LatestIngestionSuccessTime" in data:
        import capo_cloudtrail.types.date

        out["latest_ingestion_success_time"] = (
            capo_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["LatestIngestionSuccessTime"]
            )
        )
    if "LatestIngestionSuccessEventID" in data:
        out["latest_ingestion_success_event_id"] = data["LatestIngestionSuccessEventID"]
    if "LatestIngestionErrorCode" in data:
        out["latest_ingestion_error_code"] = data["LatestIngestionErrorCode"]
    if "LatestIngestionAttemptTime" in data:
        import capo_cloudtrail.types.date

        out["latest_ingestion_attempt_time"] = (
            capo_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["LatestIngestionAttemptTime"]
            )
        )
    if "LatestIngestionAttemptEventID" in data:
        out["latest_ingestion_attempt_event_id"] = data["LatestIngestionAttemptEventID"]
    return out
