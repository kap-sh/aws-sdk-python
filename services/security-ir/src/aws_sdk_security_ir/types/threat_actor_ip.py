"""Generated from Smithy shape ``com.amazonaws.securityir#ThreatActorIp``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.ip_address
    import aws_sdk_security_ir.types.user_agent


class ThreatActorIp(TypedDict):
    ip_address: "aws_sdk_security_ir.types.ip_address.IPAddress"
    """<p/>"""
    user_agent: NotRequired["aws_sdk_security_ir.types.user_agent.UserAgent"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatActorIp) -> dict:
    out: dict = {}
    out["ipAddress"] = value["ip_address"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> ThreatActorIp:
    out: ThreatActorIp = {}  # type: ignore[typeddict-item]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    else:
        raise DeserializationError("ThreatActorIp.ip_address required")
    if "userAgent" in data:
        out["user_agent"] = data["userAgent"]
    return out
