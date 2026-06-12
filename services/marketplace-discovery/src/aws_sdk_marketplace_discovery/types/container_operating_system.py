"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ContainerOperatingSystem``."""

from typing import TypedDict
from aws_sdk_marketplace_discovery.errors import DeserializationError

class ContainerOperatingSystem(TypedDict):
    operating_system_family_name: "str"
    """<p>The operating system family, such as Linux.</p>"""
    operating_system_name: "str"
    """<p>The specific operating system name.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ContainerOperatingSystem) -> dict:
    out: dict = {}
    out["operatingSystemFamilyName"] = value["operating_system_family_name"]
    out["operatingSystemName"] = value["operating_system_name"]
    return out


def deserialize_json(data: dict) -> ContainerOperatingSystem:
    out: ContainerOperatingSystem = {}  # type: ignore[typeddict-item]
    if "operatingSystemFamilyName" in data:
        out["operating_system_family_name"] = data["operatingSystemFamilyName"]
    else:
        raise DeserializationError("ContainerOperatingSystem.operating_system_family_name required")
    if "operatingSystemName" in data:
        out["operating_system_name"] = data["operatingSystemName"]
    else:
        raise DeserializationError("ContainerOperatingSystem.operating_system_name required")
    return out