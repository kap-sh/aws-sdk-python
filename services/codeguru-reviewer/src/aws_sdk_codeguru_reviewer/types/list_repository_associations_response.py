"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListRepositoryAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.next_token
    import aws_sdk_codeguru_reviewer.types.repository_association_summaries


class ListRepositoryAssociationsResponse(TypedDict):
    repository_association_summaries: NotRequired[
        "aws_sdk_codeguru_reviewer.types.repository_association_summaries.RepositoryAssociationSummaries"
    ]
    """<p>A list of repository associations that meet the criteria of the request.</p>"""
    next_token: NotRequired["aws_sdk_codeguru_reviewer.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListRecommendations</code> request. When the results of a <code>ListRecommendations</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRepositoryAssociationsResponse) -> dict:
    out: dict = {}
    if "repository_association_summaries" in value:
        import aws_sdk_codeguru_reviewer.types.repository_association_summaries

        out["RepositoryAssociationSummaries"] = (
            aws_sdk_codeguru_reviewer.types.repository_association_summaries.serialize_json(
                value["repository_association_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRepositoryAssociationsResponse:
    out: ListRepositoryAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "RepositoryAssociationSummaries" in data:
        import aws_sdk_codeguru_reviewer.types.repository_association_summaries

        out["repository_association_summaries"] = (
            aws_sdk_codeguru_reviewer.types.repository_association_summaries.deserialize_json(
                data["RepositoryAssociationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
