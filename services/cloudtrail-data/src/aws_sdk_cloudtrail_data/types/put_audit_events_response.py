"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#PutAuditEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail_data.types.audit_event_result_entries
    import aws_sdk_cloudtrail_data.types.result_error_entries


class PutAuditEventsResponse(TypedDict):
    successful: "aws_sdk_cloudtrail_data.types.audit_event_result_entries.AuditEventResultEntries"
    """<p>Lists events in the provided event payload that were successfully ingested into CloudTrail.</p>"""
    failed: "aws_sdk_cloudtrail_data.types.result_error_entries.ResultErrorEntries"
    """<p>Lists events in the provided event payload that could not be ingested into CloudTrail, and includes the error code and error message returned for events that could not be ingested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAuditEventsResponse) -> dict:
    out: dict = {}
    import aws_sdk_cloudtrail_data.types.audit_event_result_entries

    out["successful"] = (
        aws_sdk_cloudtrail_data.types.audit_event_result_entries.serialize_json(
            value["successful"]
        )
    )
    import aws_sdk_cloudtrail_data.types.result_error_entries

    out["failed"] = aws_sdk_cloudtrail_data.types.result_error_entries.serialize_json(
        value["failed"]
    )
    return out


def deserialize_json(data: dict) -> PutAuditEventsResponse:
    out: PutAuditEventsResponse = {}  # type: ignore[typeddict-item]
    if "successful" in data:
        import aws_sdk_cloudtrail_data.types.audit_event_result_entries

        out["successful"] = (
            aws_sdk_cloudtrail_data.types.audit_event_result_entries.deserialize_json(
                data["successful"]
            )
        )
    else:
        raise DeserializationError("PutAuditEventsResponse.successful required")
    if "failed" in data:
        import aws_sdk_cloudtrail_data.types.result_error_entries

        out["failed"] = (
            aws_sdk_cloudtrail_data.types.result_error_entries.deserialize_json(
                data["failed"]
            )
        )
    else:
        raise DeserializationError("PutAuditEventsResponse.failed required")
    return out
