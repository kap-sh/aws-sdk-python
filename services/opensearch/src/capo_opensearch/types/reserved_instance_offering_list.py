"""Generated from Smithy shape ``com.amazonaws.opensearch#ReservedInstanceOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.reserved_instance_offering

ReservedInstanceOfferingList: TypeAlias = list[
    "capo_opensearch.types.reserved_instance_offering.ReservedInstanceOffering"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedInstanceOfferingList) -> list:
    import capo_opensearch.types.reserved_instance_offering

    out: list = []
    for item in value:
        out.append(
            capo_opensearch.types.reserved_instance_offering.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReservedInstanceOfferingList:
    import capo_opensearch.types.reserved_instance_offering

    out: ReservedInstanceOfferingList = []
    for item in data:
        out.append(
            capo_opensearch.types.reserved_instance_offering.deserialize_json(item)
        )
    return out
