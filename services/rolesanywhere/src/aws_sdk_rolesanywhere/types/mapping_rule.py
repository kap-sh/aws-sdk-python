"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#MappingRule``."""

from typing import TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError


class MappingRule(TypedDict):
    specifier: "str"
    """<p>Specifier within a certificate field, such as CN, OU, or UID from the Subject field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MappingRule) -> dict:
    out: dict = {}
    out["specifier"] = value["specifier"]
    return out


def deserialize_json(data: dict) -> MappingRule:
    out: MappingRule = {}  # type: ignore[typeddict-item]
    if "specifier" in data:
        out["specifier"] = data["specifier"]
    else:
        raise DeserializationError("MappingRule.specifier required")
    return out
