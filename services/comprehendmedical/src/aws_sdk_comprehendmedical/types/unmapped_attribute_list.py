"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#UnmappedAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.unmapped_attribute

UnmappedAttributeList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.unmapped_attribute.UnmappedAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnmappedAttributeList) -> list:
    import aws_sdk_comprehendmedical.types.unmapped_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.unmapped_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnmappedAttributeList:
    import aws_sdk_comprehendmedical.types.unmapped_attribute

    out: UnmappedAttributeList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.unmapped_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
