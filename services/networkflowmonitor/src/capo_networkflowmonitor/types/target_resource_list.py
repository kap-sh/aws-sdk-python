"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.target_resource

TargetResourceList: TypeAlias = list[
    "capo_networkflowmonitor.types.target_resource.TargetResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetResourceList) -> list:
    import capo_networkflowmonitor.types.target_resource

    out: list = []
    for item in value:
        out.append(capo_networkflowmonitor.types.target_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetResourceList:
    import capo_networkflowmonitor.types.target_resource

    out: TargetResourceList = []
    for item in data:
        out.append(capo_networkflowmonitor.types.target_resource.deserialize_json(item))
    return out
