"""Generated from Smithy shape ``com.amazonaws.opensearch#InstanceTypeDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.instance_type_details

InstanceTypeDetailsList: TypeAlias = list[
    "capo_opensearch.types.instance_type_details.InstanceTypeDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeDetailsList) -> list:
    import capo_opensearch.types.instance_type_details

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.instance_type_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstanceTypeDetailsList:
    import capo_opensearch.types.instance_type_details

    out: InstanceTypeDetailsList = []
    for item in data:
        out.append(capo_opensearch.types.instance_type_details.deserialize_json(item))
    return out
