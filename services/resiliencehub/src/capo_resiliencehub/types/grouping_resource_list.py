"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.grouping_resource

GroupingResourceList: TypeAlias = list[
    "capo_resiliencehub.types.grouping_resource.GroupingResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingResourceList) -> list:
    import capo_resiliencehub.types.grouping_resource

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.grouping_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupingResourceList:
    import capo_resiliencehub.types.grouping_resource

    out: GroupingResourceList = []
    for item in data:
        out.append(capo_resiliencehub.types.grouping_resource.deserialize_json(item))
    return out
