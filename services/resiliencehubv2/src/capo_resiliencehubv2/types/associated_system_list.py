"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssociatedSystemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.associated_system

AssociatedSystemList: TypeAlias = list[
    "capo_resiliencehubv2.types.associated_system.AssociatedSystem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSystemList) -> list:
    import capo_resiliencehubv2.types.associated_system

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.associated_system.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedSystemList:
    import capo_resiliencehubv2.types.associated_system

    out: AssociatedSystemList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.associated_system.deserialize_json(item))
    return out
