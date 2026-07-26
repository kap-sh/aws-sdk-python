"""Generated from Smithy shape ``com.amazonaws.acm#CustomAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.custom_attribute

CustomAttributeList: TypeAlias = list["capo_acm.types.custom_attribute.CustomAttribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomAttributeList) -> list:
    import capo_acm.types.custom_attribute

    out: list = []
    for item in value:
        out.append(capo_acm.types.custom_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomAttributeList:
    import capo_acm.types.custom_attribute

    out: CustomAttributeList = []
    for item in data:
        out.append(capo_acm.types.custom_attribute.deserialize_aws_json_1_1(item))
    return out
