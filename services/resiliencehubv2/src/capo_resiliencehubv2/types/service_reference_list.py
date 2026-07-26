"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_reference

ServiceReferenceList: TypeAlias = list[
    "capo_resiliencehubv2.types.service_reference.ServiceReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceReferenceList) -> list:
    import capo_resiliencehubv2.types.service_reference

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.service_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceReferenceList:
    import capo_resiliencehubv2.types.service_reference

    out: ServiceReferenceList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.service_reference.deserialize_json(item))
    return out
