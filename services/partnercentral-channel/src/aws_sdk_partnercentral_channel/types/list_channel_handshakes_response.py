"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListChannelHandshakesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.channel_handshake_summaries
    import aws_sdk_partnercentral_channel.types.next_token


class ListChannelHandshakesResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_partnercentral_channel.types.channel_handshake_summaries.ChannelHandshakeSummaries"
    ]
    """<p>List of channel handshakes matching the criteria.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results, if available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListChannelHandshakesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_partnercentral_channel.types.channel_handshake_summaries

        out["items"] = (
            aws_sdk_partnercentral_channel.types.channel_handshake_summaries.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListChannelHandshakesResponse:
    out: ListChannelHandshakesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_partnercentral_channel.types.channel_handshake_summaries

        out["items"] = (
            aws_sdk_partnercentral_channel.types.channel_handshake_summaries.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
