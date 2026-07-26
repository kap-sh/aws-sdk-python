"""Generated from Smithy shape ``com.amazonaws.mediatailor#KeyValuePair``."""

from typing_extensions import TypedDict

from capo_mediatailor.errors import DeserializationError


class KeyValuePair(TypedDict, closed=True):
    key: "str"
    """<p>For <code>SCTE35_ENHANCED</code> output, defines a key. MediaTailor takes this key, and its associated value, and generates the key/value pair within the <code>EXT-X-ASSET</code>tag. If you specify a key, you must also specify a corresponding value.</p>"""
    value: "str"
    """<p>For <code>SCTE35_ENHANCED</code> output, defines a value. MediaTailor; takes this value, and its associated key, and generates the key/value pair within the <code>EXT-X-ASSET</code>tag. If you specify a value, you must also specify a corresponding key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyValuePair) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KeyValuePair:
    out: KeyValuePair = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("KeyValuePair.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("KeyValuePair.value required")
    return out
