"""Generated from Smithy shape ``com.amazonaws.iot#ListScheduledAuditsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.scheduled_audit_metadata_list


class ListScheduledAuditsResponse(TypedDict, closed=True):
    scheduled_audits: NotRequired[
        "aws_sdk_iot.types.scheduled_audit_metadata_list.ScheduledAuditMetadataList"
    ]
    """<p>The list of scheduled audits.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScheduledAuditsResponse) -> dict:
    out: dict = {}
    if "scheduled_audits" in value:
        import aws_sdk_iot.types.scheduled_audit_metadata_list

        out["scheduledAudits"] = (
            aws_sdk_iot.types.scheduled_audit_metadata_list.serialize_json(
                value["scheduled_audits"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScheduledAuditsResponse:
    out: ListScheduledAuditsResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAudits" in data:
        import aws_sdk_iot.types.scheduled_audit_metadata_list

        out["scheduled_audits"] = (
            aws_sdk_iot.types.scheduled_audit_metadata_list.deserialize_json(
                data["scheduledAudits"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
