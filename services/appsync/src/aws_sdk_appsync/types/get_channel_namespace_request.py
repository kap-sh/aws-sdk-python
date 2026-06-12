"""Generated from Smithy shape ``com.amazonaws.appsync#GetChannelNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.namespace
    import aws_sdk_appsync.types.string


class GetChannelNamespaceRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The <code>Api</code> ID.</p>"""
    name: "aws_sdk_appsync.types.namespace.Namespace"
    """<p>The name of the <code>ChannelNamespace</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelNamespaceRequest:
    out: GetChannelNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
