"""Generated from Smithy shape ``com.amazonaws.datazone#LineageEventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.event_summary
    import capo_datazone.types.lineage_event_identifier
    import capo_datazone.types.lineage_event_processing_status


class LineageEventSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_datazone.types.lineage_event_identifier.LineageEventIdentifier"
    ]
    """<p>The ID of the data lineage event.</p>"""
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The domain ID of the lineage event.</p>"""
    processing_status: NotRequired[
        "capo_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
    ]
    """<p>The processing status of the data lineage event.</p>"""
    event_time: NotRequired["datetime.datetime"]
    """<p>The time of the data lineage event.</p>"""
    event_summary: NotRequired["capo_datazone.types.event_summary.EventSummary"]
    """<p>The summary of the data lineate event.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data lineage event.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which data lineage event was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageEventSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "processing_status" in value:
        import capo_datazone.types.lineage_event_processing_status

        out["processingStatus"] = (
            capo_datazone.types.lineage_event_processing_status.serialize_json(
                value["processing_status"]
            )
        )
    if "event_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["eventTime"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["event_time"]
        )
    if "event_summary" in value:
        import capo_datazone.types.event_summary

        out["eventSummary"] = capo_datazone.types.event_summary.serialize_json(
            value["event_summary"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> LineageEventSummary:
    out: LineageEventSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "processingStatus" in data:
        import capo_datazone.types.lineage_event_processing_status

        out["processing_status"] = (
            capo_datazone.types.lineage_event_processing_status.deserialize_json(
                data["processingStatus"]
            )
        )
    if "eventTime" in data:
        import capo_datazone.types._prelude.timestamp

        out["event_time"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["eventTime"]
        )
    if "eventSummary" in data:
        import capo_datazone.types.event_summary

        out["event_summary"] = capo_datazone.types.event_summary.deserialize_json(
            data["eventSummary"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    return out
