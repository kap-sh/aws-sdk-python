"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_resource

ServiceResourceList: TypeAlias = list[
    "capo_resiliencehubv2.types.service_resource.ServiceResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourceList) -> list:
    import capo_resiliencehubv2.types.service_resource

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.service_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceResourceList:
    import capo_resiliencehubv2.types.service_resource

    out: ServiceResourceList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.service_resource.deserialize_json(item))
    return out
