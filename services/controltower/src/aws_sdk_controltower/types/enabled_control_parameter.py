"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlParameter``."""

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError


class EnabledControlParameter(TypedDict, closed=True):
    key: "str"
    """<p>The key of a key/value pair.</p>"""
    value: "object"
    """<p>The value of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlParameter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EnabledControlParameter:
    out: EnabledControlParameter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("EnabledControlParameter.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EnabledControlParameter.value required")
    return out
