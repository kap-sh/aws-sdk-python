"""Generated from Smithy shape ``com.amazonaws.ivs#StreamFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.stream_health


class StreamFilters(TypedDict, closed=True):
    health: NotRequired["capo_ivs.types.stream_health.StreamHealth"]
    """<p>The stream’s health.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamFilters) -> dict:
    out: dict = {}
    if "health" in value:
        out["health"] = value["health"]
    return out


def deserialize_json(data: dict) -> StreamFilters:
    out: StreamFilters = {}  # type: ignore[typeddict-item]
    if "health" in data:
        out["health"] = data["health"]
    return out
