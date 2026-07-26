"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35DescriptorSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.scte35_segmentation_descriptor


class Scte35DescriptorSettings(TypedDict, closed=True):
    segmentation_descriptor_scte35_descriptor_settings: NotRequired[
        "capo_medialive.types.scte35_segmentation_descriptor.Scte35SegmentationDescriptor"
    ]
    """SCTE-35 Segmentation Descriptor."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35DescriptorSettings) -> dict:
    out: dict = {}
    if "segmentation_descriptor_scte35_descriptor_settings" in value:
        import capo_medialive.types.scte35_segmentation_descriptor

        out["segmentationDescriptorScte35DescriptorSettings"] = (
            capo_medialive.types.scte35_segmentation_descriptor.serialize_json(
                value["segmentation_descriptor_scte35_descriptor_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Scte35DescriptorSettings:
    out: Scte35DescriptorSettings = {}  # type: ignore[typeddict-item]
    if "segmentationDescriptorScte35DescriptorSettings" in data:
        import capo_medialive.types.scte35_segmentation_descriptor

        out["segmentation_descriptor_scte35_descriptor_settings"] = (
            capo_medialive.types.scte35_segmentation_descriptor.deserialize_json(
                data["segmentationDescriptorScte35DescriptorSettings"]
            )
        )
    return out
