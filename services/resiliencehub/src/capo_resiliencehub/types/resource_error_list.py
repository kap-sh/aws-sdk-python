"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.resource_error

ResourceErrorList: TypeAlias = list[
    "capo_resiliencehub.types.resource_error.ResourceError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceErrorList) -> list:
    import capo_resiliencehub.types.resource_error

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.resource_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceErrorList:
    import capo_resiliencehub.types.resource_error

    out: ResourceErrorList = []
    for item in data:
        out.append(capo_resiliencehub.types.resource_error.deserialize_json(item))
    return out
