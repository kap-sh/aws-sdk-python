"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectAttributeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_attribute_range

ObjectAttributeRangeList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.object_attribute_range.ObjectAttributeRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttributeRangeList) -> list:
    import aws_sdk_clouddirectory.types.object_attribute_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.object_attribute_range.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ObjectAttributeRangeList:
    import aws_sdk_clouddirectory.types.object_attribute_range

    out: ObjectAttributeRangeList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.object_attribute_range.deserialize_json(item)
        )
    return out
