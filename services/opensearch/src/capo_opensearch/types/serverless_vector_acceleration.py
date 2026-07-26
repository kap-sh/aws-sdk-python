"""Generated from Smithy shape ``com.amazonaws.opensearch#ServerlessVectorAcceleration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean


class ServerlessVectorAcceleration(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Specifies whether serverless vector acceleration is enabled for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessVectorAcceleration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ServerlessVectorAcceleration:
    out: ServerlessVectorAcceleration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
