"""Generated from Smithy shape ``com.amazonaws.fms#App``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.ip_port_number
    import aws_sdk_fms.types.protocol
    import aws_sdk_fms.types.resource_name


class App(TypedDict):
    app_name: "aws_sdk_fms.types.resource_name.ResourceName"
    """<p>The application's name.</p>"""
    protocol: "aws_sdk_fms.types.protocol.Protocol"
    r"""<p>The IP protocol name or number. The name can be one of <code>tcp</code>, <code>udp</code>, or <code>icmp</code>. For information on possible numbers, see <a href=\"https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers</a>.</p>"""
    port: "aws_sdk_fms.types.ip_port_number.IPPortNumber"
    """<p>The application's port number, for example <code>80</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: App) -> dict:
    out: dict = {}
    out["AppName"] = value["app_name"]
    out["Protocol"] = value["protocol"]
    out["Port"] = value["port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> App:
    out: App = {}  # type: ignore[typeddict-item]
    if "AppName" in data:
        out["app_name"] = data["AppName"]
    else:
        raise DeserializationError("App.app_name required")
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    else:
        raise DeserializationError("App.protocol required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("App.port required")
    return out
