"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourcePriority``."""

from typing_extensions import NotRequired, TypedDict


class SourcePriority(TypedDict, closed=True):
    primary_source: NotRequired["str"]
    """<p> The name of the source you choose as the primary source for this flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourcePriority) -> dict:
    out: dict = {}
    if "primary_source" in value:
        out["primarySource"] = value["primary_source"]
    return out


def deserialize_json(data: dict) -> SourcePriority:
    out: SourcePriority = {}  # type: ignore[typeddict-item]
    if "primarySource" in data:
        out["primary_source"] = data["primarySource"]
    return out
