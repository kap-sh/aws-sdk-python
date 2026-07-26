"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceDriftList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.resource_drift

ResourceDriftList: TypeAlias = list[
    "capo_resiliencehub.types.resource_drift.ResourceDrift"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDriftList) -> list:
    import capo_resiliencehub.types.resource_drift

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.resource_drift.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceDriftList:
    import capo_resiliencehub.types.resource_drift

    out: ResourceDriftList = []
    for item in data:
        out.append(capo_resiliencehub.types.resource_drift.deserialize_json(item))
    return out
