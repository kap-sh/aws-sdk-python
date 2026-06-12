"""Generated from Smithy shape ``com.amazonaws.greengrass#ConnectivityInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__integer
    import aws_sdk_greengrass.types.__string


class ConnectivityInfo(TypedDict):
    host_address: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The endpoint for the Greengrass core. Can be an IP address or DNS."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the connectivity information."""
    metadata: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """Metadata for this endpoint."""
    port_number: NotRequired["aws_sdk_greengrass.types.__integer.__integer"]
    """The port of the Greengrass core. Usually 8883."""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityInfo) -> dict:
    out: dict = {}
    if "host_address" in value:
        out["HostAddress"] = value["host_address"]
    if "id" in value:
        out["Id"] = value["id"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "port_number" in value:
        out["PortNumber"] = value["port_number"]
    return out


def deserialize_json(data: dict) -> ConnectivityInfo:
    out: ConnectivityInfo = {}  # type: ignore[typeddict-item]
    if "HostAddress" in data:
        out["host_address"] = data["HostAddress"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "PortNumber" in data:
        out["port_number"] = data["PortNumber"]
    return out
