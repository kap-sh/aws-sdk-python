"""Generated from Smithy shape ``com.amazonaws.appsync#ListChannelNamespacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.channel_namespaces
    import aws_sdk_appsync.types.pagination_token


class ListChannelNamespacesResponse(TypedDict):
    channel_namespaces: NotRequired[
        "aws_sdk_appsync.types.channel_namespaces.ChannelNamespaces"
    ]
    """<p>The <code>ChannelNamespace</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelNamespacesResponse) -> dict:
    out: dict = {}
    if "channel_namespaces" in value:
        import aws_sdk_appsync.types.channel_namespaces

        out["channelNamespaces"] = (
            aws_sdk_appsync.types.channel_namespaces.serialize_json(
                value["channel_namespaces"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelNamespacesResponse:
    out: ListChannelNamespacesResponse = {}  # type: ignore[typeddict-item]
    if "channelNamespaces" in data:
        import aws_sdk_appsync.types.channel_namespaces

        out["channel_namespaces"] = (
            aws_sdk_appsync.types.channel_namespaces.deserialize_json(
                data["channelNamespaces"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
