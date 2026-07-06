"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListTracksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.track_list


class ListTracksResponse(TypedDict, closed=True):
    tracks: NotRequired["aws_sdk_redshift_serverless.types.track_list.TrackList"]
    """<p>The returned tracks.</p>"""
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTracksResponse) -> dict:
    out: dict = {}
    if "tracks" in value:
        import aws_sdk_redshift_serverless.types.track_list

        out["tracks"] = (
            aws_sdk_redshift_serverless.types.track_list.serialize_aws_json_1_1(
                value["tracks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTracksResponse:
    out: ListTracksResponse = {}  # type: ignore[typeddict-item]
    if "tracks" in data:
        import aws_sdk_redshift_serverless.types.track_list

        out["tracks"] = (
            aws_sdk_redshift_serverless.types.track_list.deserialize_aws_json_1_1(
                data["tracks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
