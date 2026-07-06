"""Generated from Smithy shape ``com.amazonaws.datazone#SearchGroupProfilesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.group_profile_summaries
    import aws_sdk_datazone.types.pagination_token


class SearchGroupProfilesOutput(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_datazone.types.group_profile_summaries.GroupProfileSummaries"
    ]
    """<p>The results of the <code>SearchGroupProfiles</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchGroupProfiles</code> to list the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupProfilesOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.group_profile_summaries

        out["items"] = aws_sdk_datazone.types.group_profile_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchGroupProfilesOutput:
    out: SearchGroupProfilesOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.group_profile_summaries

        out["items"] = aws_sdk_datazone.types.group_profile_summaries.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
