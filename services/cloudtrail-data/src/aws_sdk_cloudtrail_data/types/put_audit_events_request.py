"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#PutAuditEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail_data.types.audit_events
    import aws_sdk_cloudtrail_data.types.channel_arn
    import aws_sdk_cloudtrail_data.types.external_id


class PutAuditEventsRequest(TypedDict, closed=True):
    audit_events: "aws_sdk_cloudtrail_data.types.audit_events.AuditEvents"
    """<p>The JSON payload of events that you want to ingest. You can also point to the JSON event payload in a file.</p>"""
    channel_arn: "aws_sdk_cloudtrail_data.types.channel_arn.ChannelArn"
    """<p>The ARN or ID (the ARN suffix) of a channel.</p>"""
    external_id: NotRequired["aws_sdk_cloudtrail_data.types.external_id.ExternalId"]
    """<p>A unique identifier that is conditionally required when the channel's resource policy includes an external ID. This value can be any string, such as a passphrase or account number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAuditEventsRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudtrail_data.types.audit_events

    out["auditEvents"] = aws_sdk_cloudtrail_data.types.audit_events.serialize_json(
        value["audit_events"]
    )
    return out


def deserialize_json(data: dict) -> PutAuditEventsRequest:
    out: PutAuditEventsRequest = {}  # type: ignore[typeddict-item]
    if "auditEvents" in data:
        import aws_sdk_cloudtrail_data.types.audit_events

        out["audit_events"] = (
            aws_sdk_cloudtrail_data.types.audit_events.deserialize_json(
                data["auditEvents"]
            )
        )
    else:
        raise DeserializationError("PutAuditEventsRequest.audit_events required")
    return out
