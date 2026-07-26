"""Generated from Smithy shape ``com.amazonaws.lightsail#PartnerIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.non_empty_string

PartnerIdList: TypeAlias = list["capo_lightsail.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PartnerIdList:
    return list(data)
