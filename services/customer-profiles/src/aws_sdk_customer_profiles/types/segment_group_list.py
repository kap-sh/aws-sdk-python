"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.group

SegmentGroupList: TypeAlias = list["aws_sdk_customer_profiles.types.group.Group"]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentGroupList) -> list:
    import aws_sdk_customer_profiles.types.group

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SegmentGroupList:
    import aws_sdk_customer_profiles.types.group

    out: SegmentGroupList = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.group.deserialize_json(item))
    return out
