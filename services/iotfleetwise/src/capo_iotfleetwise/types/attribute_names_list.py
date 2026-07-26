"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#attributeNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.attribute_name

attributeNamesList: TypeAlias = list[
    "capo_iotfleetwise.types.attribute_name.attributeName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: attributeNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> attributeNamesList:
    return list(data)
