"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgramServiceDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_max256


class MultiplexProgramServiceDescriptor(TypedDict, closed=True):
    provider_name: NotRequired["aws_sdk_medialive.types.__string_max256.__stringMax256"]
    """Name of the provider."""
    service_name: NotRequired["aws_sdk_medialive.types.__string_max256.__stringMax256"]
    """Name of the service."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgramServiceDescriptor) -> dict:
    out: dict = {}
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    return out


def deserialize_json(data: dict) -> MultiplexProgramServiceDescriptor:
    out: MultiplexProgramServiceDescriptor = {}  # type: ignore[typeddict-item]
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    return out
