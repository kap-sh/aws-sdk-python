"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.channels
    import capo_cloudtrail.types.pagination_token


class ListChannelsResponse(TypedDict, closed=True):
    channels: NotRequired["capo_cloudtrail.types.channels.Channels"]
    """<p> The list of channels in the account. </p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>The token to use to get the next page of results after a previous API call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_cloudtrail.types.channels

        out["Channels"] = capo_cloudtrail.types.channels.serialize_aws_json_1_1(
            value["channels"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if "Channels" in data:
        import capo_cloudtrail.types.channels

        out["channels"] = capo_cloudtrail.types.channels.deserialize_aws_json_1_1(
            data["Channels"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
