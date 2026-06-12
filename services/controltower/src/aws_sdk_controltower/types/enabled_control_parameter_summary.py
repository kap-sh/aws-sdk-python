"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlParameterSummary``."""

from typing import TypedDict

from aws_sdk_controltower.errors import DeserializationError


class EnabledControlParameterSummary(TypedDict):
    key: "str"
    """<p>The key of a key/value pair.</p>"""
    value: "object"
    """<p>The value of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlParameterSummary) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EnabledControlParameterSummary:
    out: EnabledControlParameterSummary = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("EnabledControlParameterSummary.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EnabledControlParameterSummary.value required")
    return out
