"""Generated from Smithy shape ``com.amazonaws.datazone#ListProjectProfilesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_profile_summaries


class ListProjectProfilesOutput(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_datazone.types.project_profile_summaries.ProjectProfileSummaries"
    ]
    """<p>The results of the ListProjectProfiles action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of project profiles is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of project profiles, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListProjectProfiles to list the next set of project profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectProfilesOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.project_profile_summaries

        out["items"] = aws_sdk_datazone.types.project_profile_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectProfilesOutput:
    out: ListProjectProfilesOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.project_profile_summaries

        out["items"] = (
            aws_sdk_datazone.types.project_profile_summaries.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
