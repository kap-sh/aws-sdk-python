"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListProjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.next_token
    import aws_sdk_iotsitewise.types.project_summaries


class ListProjectsResponse(TypedDict, closed=True):
    project_summaries: "aws_sdk_iotsitewise.types.project_summaries.ProjectSummaries"
    """<p>A list that summarizes each project in the portal.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.project_summaries

    out["projectSummaries"] = (
        aws_sdk_iotsitewise.types.project_summaries.serialize_json(
            value["project_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectsResponse:
    out: ListProjectsResponse = {}  # type: ignore[typeddict-item]
    if "projectSummaries" in data:
        import aws_sdk_iotsitewise.types.project_summaries

        out["project_summaries"] = (
            aws_sdk_iotsitewise.types.project_summaries.deserialize_json(
                data["projectSummaries"]
            )
        )
    else:
        raise DeserializationError("ListProjectsResponse.project_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
