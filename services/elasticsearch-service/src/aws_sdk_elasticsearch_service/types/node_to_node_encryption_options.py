"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#NodeToNodeEncryptionOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean


class NodeToNodeEncryptionOptions(TypedDict):
    enabled: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>Specify true to enable node-to-node encryption.</p>"""


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
