"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseAuditEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.audit_events_list
    import aws_sdk_connectcases.types.next_token


class GetCaseAuditEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""
    audit_events: "aws_sdk_connectcases.types.audit_events_list.AuditEventsList"
    """<p>A list of case audits where each represents a particular edit of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAuditEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_connectcases.types.audit_events_list

    out["auditEvents"] = aws_sdk_connectcases.types.audit_events_list.serialize_json(
        value["audit_events"]
    )
    return out


def deserialize_json(data: dict) -> GetCaseAuditEventsResponse:
    out: GetCaseAuditEventsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "auditEvents" in data:
        import aws_sdk_connectcases.types.audit_events_list

        out["audit_events"] = (
            aws_sdk_connectcases.types.audit_events_list.deserialize_json(
                data["auditEvents"]
            )
        )
    else:
        raise DeserializationError("GetCaseAuditEventsResponse.audit_events required")
    return out
