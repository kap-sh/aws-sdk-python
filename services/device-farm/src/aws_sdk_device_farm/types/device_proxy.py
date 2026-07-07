"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceProxy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_proxy_host
    import aws_sdk_device_farm.types.device_proxy_port


class DeviceProxy(TypedDict, closed=True):
    host: "aws_sdk_device_farm.types.device_proxy_host.DeviceProxyHost"
    """<p>Hostname or IPv4 address of the proxy.</p>"""
    port: "aws_sdk_device_farm.types.device_proxy_port.DeviceProxyPort"
    """<p>The port number on which the http/s proxy is listening.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceProxy) -> dict:
    out: dict = {}
    out["host"] = value["host"]
    out["port"] = value.get("port", 3128)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceProxy:
    out: DeviceProxy = {}  # type: ignore[typeddict-item]
    if "host" in data:
        out["host"] = data["host"]
    else:
        raise DeserializationError("DeviceProxy.host required")
    if "port" in data:
        out["port"] = data["port"]
    else:
        out["port"] = 3128
    return out
