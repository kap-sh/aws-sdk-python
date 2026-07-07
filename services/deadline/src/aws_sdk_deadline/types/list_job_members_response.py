"""Generated from Smithy shape ``com.amazonaws.deadline#ListJobMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_members
    import aws_sdk_deadline.types.next_token


class ListJobMembersResponse(TypedDict, closed=True):
    members: "aws_sdk_deadline.types.job_members.JobMembers"
    """<p>The members on the list.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobMembersResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.job_members

    out["members"] = aws_sdk_deadline.types.job_members.serialize_json(value["members"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobMembersResponse:
    out: ListJobMembersResponse = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import aws_sdk_deadline.types.job_members

        out["members"] = aws_sdk_deadline.types.job_members.deserialize_json(
            data["members"]
        )
    else:
        raise DeserializationError("ListJobMembersResponse.members required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
