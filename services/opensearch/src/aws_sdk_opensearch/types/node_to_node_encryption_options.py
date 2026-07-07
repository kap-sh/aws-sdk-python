"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeToNodeEncryptionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean


class NodeToNodeEncryptionOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True to enable node-to-node encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeToNodeEncryptionOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> NodeToNodeEncryptionOptions:
    out: NodeToNodeEncryptionOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
