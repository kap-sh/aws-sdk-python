"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceReference``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ServiceReference(TypedDict):
    service_id: NotRequired["str"]
    """<p>The identifier of the referenced service.</p>"""
    service_name: NotRequired["str"]
    """<p>The name of the referenced service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceReference) -> dict:
    out: dict = {}
    if "service_id" in value:
        out["serviceId"] = value["service_id"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    return out


def deserialize_json(data: dict) -> ServiceReference:
    out: ServiceReference = {}  # type: ignore[typeddict-item]
    if "serviceId" in data:
        out["service_id"] = data["serviceId"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    return out
