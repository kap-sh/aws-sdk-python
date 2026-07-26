"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UnsupportedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.unsupported_resource

UnsupportedResourceList: TypeAlias = list[
    "capo_resiliencehub.types.unsupported_resource.UnsupportedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedResourceList) -> list:
    import capo_resiliencehub.types.unsupported_resource

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.unsupported_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnsupportedResourceList:
    import capo_resiliencehub.types.unsupported_resource

    out: UnsupportedResourceList = []
    for item in data:
        out.append(capo_resiliencehub.types.unsupported_resource.deserialize_json(item))
    return out
