"""Generated from Smithy shape ``com.amazonaws.groundstation#IntegerRange``."""

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError


class IntegerRange(TypedDict, closed=True):
    minimum: "int"
    """<p>A minimum value.</p>"""
    maximum: "int"
    """<p>A maximum value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerRange) -> dict:
    out: dict = {}
    out["minimum"] = value["minimum"]
    out["maximum"] = value["maximum"]
    return out


def deserialize_json(data: dict) -> IntegerRange:
    out: IntegerRange = {}  # type: ignore[typeddict-item]
    if "minimum" in data:
        out["minimum"] = data["minimum"]
    else:
        raise DeserializationError("IntegerRange.minimum required")
    if "maximum" in data:
        out["maximum"] = data["maximum"]
    else:
        raise DeserializationError("IntegerRange.maximum required")
    return out
