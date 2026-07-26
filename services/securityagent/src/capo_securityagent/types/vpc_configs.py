"""Generated from Smithy shape ``com.amazonaws.securityagent#VpcConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.vpc_config

VpcConfigs: TypeAlias = list["capo_securityagent.types.vpc_config.VpcConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigs) -> list:
    import capo_securityagent.types.vpc_config

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.vpc_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> VpcConfigs:
    import capo_securityagent.types.vpc_config

    out: VpcConfigs = []
    for item in data:
        out.append(capo_securityagent.types.vpc_config.deserialize_json(item))
    return out
