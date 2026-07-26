"""Generated from Smithy shape ``com.amazonaws.opensearch#S3VectorsEngine``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean


class S3VectorsEngine(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Enables S3 vectors engine features.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3VectorsEngine) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> S3VectorsEngine:
    out: S3VectorsEngine = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
