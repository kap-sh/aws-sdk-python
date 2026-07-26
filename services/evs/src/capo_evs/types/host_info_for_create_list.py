"""Generated from Smithy shape ``com.amazonaws.evs#HostInfoForCreateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.host_info_for_create

HostInfoForCreateList: TypeAlias = list[
    "capo_evs.types.host_info_for_create.HostInfoForCreate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostInfoForCreateList) -> list:
    import capo_evs.types.host_info_for_create

    out: list = []
    for item in value:
        out.append(capo_evs.types.host_info_for_create.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> HostInfoForCreateList:
    import capo_evs.types.host_info_for_create

    out: HostInfoForCreateList = []
    for item in data:
        out.append(capo_evs.types.host_info_for_create.deserialize_aws_json_1_0(item))
    return out
