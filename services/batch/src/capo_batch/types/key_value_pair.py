"""Generated from Smithy shape ``com.amazonaws.batch#KeyValuePair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class KeyValuePair(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the key-value pair. For environment variables, this is the name of the environment variable.</p>"""
    value: NotRequired["capo_batch.types.string.String"]
    """<p>The value of the key-value pair. For environment variables, this is the value of the environment variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyValuePair) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KeyValuePair:
    out: KeyValuePair = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
