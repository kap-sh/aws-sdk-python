"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_task_metadata_list
    import aws_sdk_iot.types.next_token


class ListAuditTasksResponse(TypedDict):
    tasks: NotRequired[
        "aws_sdk_iot.types.audit_task_metadata_list.AuditTaskMetadataList"
    ]
    """<p>The audits that were performed during the specified time period.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditTasksResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import aws_sdk_iot.types.audit_task_metadata_list

        out["tasks"] = aws_sdk_iot.types.audit_task_metadata_list.serialize_json(
            value["tasks"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditTasksResponse:
    out: ListAuditTasksResponse = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_iot.types.audit_task_metadata_list

        out["tasks"] = aws_sdk_iot.types.audit_task_metadata_list.deserialize_json(
            data["tasks"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
