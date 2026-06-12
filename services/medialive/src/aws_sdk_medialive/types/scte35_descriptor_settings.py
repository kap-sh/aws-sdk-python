"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35DescriptorSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.scte35_segmentation_descriptor


class Scte35DescriptorSettings(TypedDict):
    segmentation_descriptor_scte35_descriptor_settings: NotRequired[
        "aws_sdk_medialive.types.scte35_segmentation_descriptor.Scte35SegmentationDescriptor"
    ]
    """SCTE-35 Segmentation Descriptor."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35DescriptorSettings) -> dict:
    out: dict = {}
    if "segmentation_descriptor_scte35_descriptor_settings" in value:
        import aws_sdk_medialive.types.scte35_segmentation_descriptor

        out["segmentationDescriptorScte35DescriptorSettings"] = (
            aws_sdk_medialive.types.scte35_segmentation_descriptor.serialize_json(
                value["segmentation_descriptor_scte35_descriptor_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Scte35DescriptorSettings:
    out: Scte35DescriptorSettings = {}  # type: ignore[typeddict-item]
    if "segmentationDescriptorScte35DescriptorSettings" in data:
        import aws_sdk_medialive.types.scte35_segmentation_descriptor

        out["segmentation_descriptor_scte35_descriptor_settings"] = (
            aws_sdk_medialive.types.scte35_segmentation_descriptor.deserialize_json(
                data["segmentationDescriptorScte35DescriptorSettings"]
            )
        )
    return out
