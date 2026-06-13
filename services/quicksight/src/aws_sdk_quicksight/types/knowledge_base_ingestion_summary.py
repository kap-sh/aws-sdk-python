"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseIngestionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.kb_ingestion_id
    import aws_sdk_quicksight.types.kb_ingestion_status


class KnowledgeBaseIngestionSummary(TypedDict):
    ingestion_id: "aws_sdk_quicksight.types.kb_ingestion_id.KbIngestionId"
    """<p>The unique identifier for the ingestion job.</p>"""
    ingestion_status: "aws_sdk_quicksight.types.kb_ingestion_status.KbIngestionStatus"
    """<p>The status of the ingestion job.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time of the ingestion job.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the ingestion job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseIngestionSummary) -> dict:
    out: dict = {}
    out["IngestionId"] = value["ingestion_id"]
    import aws_sdk_quicksight.types.kb_ingestion_status

    out["IngestionStatus"] = (
        aws_sdk_quicksight.types.kb_ingestion_status.serialize_json(
            value["ingestion_status"]
        )
    )
    if "start_time" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["StartTime"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["EndTime"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseIngestionSummary:
    out: KnowledgeBaseIngestionSummary = {}  # type: ignore[typeddict-item]
    if "IngestionId" in data:
        out["ingestion_id"] = data["IngestionId"]
    else:
        raise DeserializationError(
            "KnowledgeBaseIngestionSummary.ingestion_id required"
        )
    if "IngestionStatus" in data:
        import aws_sdk_quicksight.types.kb_ingestion_status

        out["ingestion_status"] = (
            aws_sdk_quicksight.types.kb_ingestion_status.deserialize_json(
                data["IngestionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBaseIngestionSummary.ingestion_status required"
        )
    if "StartTime" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["end_time"] = aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
            data["EndTime"]
        )
    return out
