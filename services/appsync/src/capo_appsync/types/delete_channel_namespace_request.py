"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteChannelNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.namespace
    import capo_appsync.types.string


class DeleteChannelNamespaceRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The ID of the <code>Api</code> associated with the <code>ChannelNamespace</code>.</p>"""
    name: "capo_appsync.types.namespace.Namespace"
    """<p>The name of the <code>ChannelNamespace</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelNamespaceRequest:
    out: DeleteChannelNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
