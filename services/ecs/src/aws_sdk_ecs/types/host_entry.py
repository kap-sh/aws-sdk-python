"""Generated from Smithy shape ``com.amazonaws.ecs#HostEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class HostEntry(TypedDict):
    hostname: "aws_sdk_ecs.types.string.String"
    """<p>The hostname to use in the <code>/etc/hosts</code> entry.</p>"""
    ip_address: "aws_sdk_ecs.types.string.String"
    """<p>The IP address to use in the <code>/etc/hosts</code> entry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostEntry) -> dict:
    out: dict = {}
    out["hostname"] = value["hostname"]
    out["ipAddress"] = value["ip_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HostEntry:
    out: HostEntry = {}  # type: ignore[typeddict-item]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    else:
        raise DeserializationError("HostEntry.hostname required")
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    else:
        raise DeserializationError("HostEntry.ip_address required")
    return out
