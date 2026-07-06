"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateChannelNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.channel_namespace


class UpdateChannelNamespaceResponse(TypedDict, closed=True):
    channel_namespace: NotRequired[
        "aws_sdk_appsync.types.channel_namespace.ChannelNamespace"
    ]
    """<p>The <code>ChannelNamespace</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelNamespaceResponse) -> dict:
    out: dict = {}
    if "channel_namespace" in value:
        import aws_sdk_appsync.types.channel_namespace

        out["channelNamespace"] = (
            aws_sdk_appsync.types.channel_namespace.serialize_json(
                value["channel_namespace"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelNamespaceResponse:
    out: UpdateChannelNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "channelNamespace" in data:
        import aws_sdk_appsync.types.channel_namespace

        out["channel_namespace"] = (
            aws_sdk_appsync.types.channel_namespace.deserialize_json(
                data["channelNamespace"]
            )
        )
    return out
