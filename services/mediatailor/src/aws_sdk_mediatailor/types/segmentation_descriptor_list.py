"""Generated from Smithy shape ``com.amazonaws.mediatailor#SegmentationDescriptorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.segmentation_descriptor

SegmentationDescriptorList: TypeAlias = list[
    "aws_sdk_mediatailor.types.segmentation_descriptor.SegmentationDescriptor"
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentationDescriptorList) -> list:
    import aws_sdk_mediatailor.types.segmentation_descriptor

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediatailor.types.segmentation_descriptor.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SegmentationDescriptorList:
    import aws_sdk_mediatailor.types.segmentation_descriptor

    out: SegmentationDescriptorList = []
    for item in data:
        out.append(
            aws_sdk_mediatailor.types.segmentation_descriptor.deserialize_json(item)
        )
    return out
