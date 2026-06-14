"""Generated from Smithy shape ``com.amazonaws.datazone#ListProjectMembershipsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_members


class ListProjectMembershipsOutput(TypedDict):
    members: "aws_sdk_datazone.types.project_members.ProjectMembers"
    """<p>The members of the project.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of memberships is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of memberships, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjectMemberships</code> to list the next set of memberships.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectMembershipsOutput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.project_members

    out["members"] = aws_sdk_datazone.types.project_members.serialize_json(
        value["members"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectMembershipsOutput:
    out: ListProjectMembershipsOutput = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import aws_sdk_datazone.types.project_members

        out["members"] = aws_sdk_datazone.types.project_members.deserialize_json(
            data["members"]
        )
    else:
        raise DeserializationError("ListProjectMembershipsOutput.members required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
