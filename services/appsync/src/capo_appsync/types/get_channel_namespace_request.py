"""Generated from Smithy shape ``com.amazonaws.appsync#GetChannelNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.namespace
    import capo_appsync.types.string


class GetChannelNamespaceRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The <code>Api</code> ID.</p>"""
    name: "capo_appsync.types.namespace.Namespace"
    """<p>The name of the <code>ChannelNamespace</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelNamespaceRequest:
    out: GetChannelNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
