"""Generated from Smithy shape ``com.amazonaws.pricing#AttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pricing.types.string

AttributeNameList: TypeAlias = list["capo_pricing.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AttributeNameList:
    return list(data)
