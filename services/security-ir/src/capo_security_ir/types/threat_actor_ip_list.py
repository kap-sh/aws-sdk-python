"""Generated from Smithy shape ``com.amazonaws.securityir#ThreatActorIpList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.threat_actor_ip

ThreatActorIpList: TypeAlias = list[
    "capo_security_ir.types.threat_actor_ip.ThreatActorIp"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatActorIpList) -> list:
    import capo_security_ir.types.threat_actor_ip

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.threat_actor_ip.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatActorIpList:
    import capo_security_ir.types.threat_actor_ip

    out: ThreatActorIpList = []
    for item in data:
        out.append(capo_security_ir.types.threat_actor_ip.deserialize_json(item))
    return out
