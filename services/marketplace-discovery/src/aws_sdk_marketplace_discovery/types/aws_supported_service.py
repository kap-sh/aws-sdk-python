"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AwsSupportedService``."""

from typing import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError


class AwsSupportedService(TypedDict):
    supported_service_type: "str"
    """<p>The machine-readable identifier of the supported service.</p>"""
    display_name: "str"
    """<p>The human-readable name of the supported service.</p>"""
    description: "str"
    """<p>A description of the supported service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSupportedService) -> dict:
    out: dict = {}
    out["supportedServiceType"] = value["supported_service_type"]
    out["displayName"] = value["display_name"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AwsSupportedService:
    out: AwsSupportedService = {}  # type: ignore[typeddict-item]
    if "supportedServiceType" in data:
        out["supported_service_type"] = data["supportedServiceType"]
    else:
        raise DeserializationError(
            "AwsSupportedService.supported_service_type required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("AwsSupportedService.display_name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("AwsSupportedService.description required")
    return out
