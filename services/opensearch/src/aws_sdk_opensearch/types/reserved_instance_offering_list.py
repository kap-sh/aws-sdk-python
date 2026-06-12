"""Generated from Smithy shape ``com.amazonaws.opensearch#ReservedInstanceOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.reserved_instance_offering

ReservedInstanceOfferingList: TypeAlias = list[
    "aws_sdk_opensearch.types.reserved_instance_offering.ReservedInstanceOffering"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedInstanceOfferingList) -> list:
    import aws_sdk_opensearch.types.reserved_instance_offering

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearch.types.reserved_instance_offering.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReservedInstanceOfferingList:
    import aws_sdk_opensearch.types.reserved_instance_offering

    out: ReservedInstanceOfferingList = []
    for item in data:
        out.append(
            aws_sdk_opensearch.types.reserved_instance_offering.deserialize_json(item)
        )
    return out
