"""Generated from Smithy shape ``com.amazonaws.frauddetector#entityTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.entity_type

entityTypeList: TypeAlias = list["capo_frauddetector.types.entity_type.EntityType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: entityTypeList) -> list:
    import capo_frauddetector.types.entity_type

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.entity_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> entityTypeList:
    import capo_frauddetector.types.entity_type

    out: entityTypeList = []
    for item in data:
        out.append(capo_frauddetector.types.entity_type.deserialize_aws_json_1_1(item))
    return out
