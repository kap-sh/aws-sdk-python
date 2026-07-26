"""Generated from Smithy shape ``com.amazonaws.backup#KeyValue``."""

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError


class KeyValue(TypedDict, closed=True):
    key: "str"
    r"""<p>The tag key (String). The key can't start with <code>aws:</code>.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 128.</p> <p>Pattern: <code>^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$</code> </p>"""
    value: "str"
    r"""<p>The value of the key.</p> <p>Length Constraints: Maximum length of 256.</p> <p>Pattern: <code>^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyValue) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KeyValue:
    out: KeyValue = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("KeyValue.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("KeyValue.value required")
    return out
