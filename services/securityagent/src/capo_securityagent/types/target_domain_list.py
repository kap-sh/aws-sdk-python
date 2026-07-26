"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.target_domain

TargetDomainList: TypeAlias = list[
    "capo_securityagent.types.target_domain.TargetDomain"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetDomainList) -> list:
    import capo_securityagent.types.target_domain

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.target_domain.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetDomainList:
    import capo_securityagent.types.target_domain

    out: TargetDomainList = []
    for item in data:
        out.append(capo_securityagent.types.target_domain.deserialize_json(item))
    return out
