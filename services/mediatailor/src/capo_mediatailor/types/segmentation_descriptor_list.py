"""Generated from Smithy shape ``com.amazonaws.mediatailor#SegmentationDescriptorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.segmentation_descriptor

SegmentationDescriptorList: TypeAlias = list[
    "capo_mediatailor.types.segmentation_descriptor.SegmentationDescriptor"
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentationDescriptorList) -> list:
    import capo_mediatailor.types.segmentation_descriptor

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.segmentation_descriptor.serialize_json(item))
    return out


def deserialize_json(data: list) -> SegmentationDescriptorList:
    import capo_mediatailor.types.segmentation_descriptor

    out: SegmentationDescriptorList = []
    for item in data:
        out.append(
            capo_mediatailor.types.segmentation_descriptor.deserialize_json(item)
        )
    return out
