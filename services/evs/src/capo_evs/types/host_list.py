"""Generated from Smithy shape ``com.amazonaws.evs#HostList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.host

HostList: TypeAlias = list["capo_evs.types.host.Host"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostList) -> list:
    import capo_evs.types.host

    out: list = []
    for item in value:
        out.append(capo_evs.types.host.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> HostList:
    import capo_evs.types.host

    out: HostList = []
    for item in data:
        out.append(capo_evs.types.host.deserialize_aws_json_1_0(item))
    return out
