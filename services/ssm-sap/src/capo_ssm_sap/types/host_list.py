"""Generated from Smithy shape ``com.amazonaws.ssmsap#HostList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.host

HostList: TypeAlias = list["capo_ssm_sap.types.host.Host"]


# --- restJson1 ser/de ---
def serialize_json(value: HostList) -> list:
    import capo_ssm_sap.types.host

    out: list = []
    for item in value:
        out.append(capo_ssm_sap.types.host.serialize_json(item))
    return out


def deserialize_json(data: list) -> HostList:
    import capo_ssm_sap.types.host

    out: HostList = []
    for item in data:
        out.append(capo_ssm_sap.types.host.deserialize_json(item))
    return out
