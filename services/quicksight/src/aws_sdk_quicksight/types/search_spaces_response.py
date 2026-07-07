"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchSpacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.next_token
    import aws_sdk_quicksight.types.public_space_arn
    import aws_sdk_quicksight.types.public_space_id
    import aws_sdk_quicksight.types.space_summaries


class SearchSpacesResponse(TypedDict, closed=True):
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["aws_sdk_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    space_summaries: "aws_sdk_quicksight.types.space_summaries.SpaceSummaries"
    """<p>A list of space summaries that match the search criteria.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpacesResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    import aws_sdk_quicksight.types.space_summaries

    out["SpaceSummaries"] = aws_sdk_quicksight.types.space_summaries.serialize_json(
        value["space_summaries"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchSpacesResponse:
    out: SearchSpacesResponse = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("SearchSpacesResponse.space_id required")
    if "spaceArn" in data:
        out["space_arn"] = data["spaceArn"]
    if "SpaceSummaries" in data:
        import aws_sdk_quicksight.types.space_summaries

        out["space_summaries"] = (
            aws_sdk_quicksight.types.space_summaries.deserialize_json(
                data["SpaceSummaries"]
            )
        )
    else:
        raise DeserializationError("SearchSpacesResponse.space_summaries required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
