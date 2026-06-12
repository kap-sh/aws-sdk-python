"""Generated from Smithy shape ``com.amazonaws.vpclattice#TxtMethodConfig``."""

from typing import TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError


class TxtMethodConfig(TypedDict):
    value: "str"
    """<p> The value that must be added to the TXT record for domain verification. </p>"""
    name: "str"
    """<p> The name of the TXT record that must be created for domain verification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TxtMethodConfig) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TxtMethodConfig:
    out: TxtMethodConfig = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TxtMethodConfig.value required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TxtMethodConfig.name required")
    return out
