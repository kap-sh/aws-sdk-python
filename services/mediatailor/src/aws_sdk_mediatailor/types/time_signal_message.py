"""Generated from Smithy shape ``com.amazonaws.mediatailor#TimeSignalMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.segmentation_descriptor_list


class TimeSignalMessage(TypedDict):
    segmentation_descriptors: NotRequired[
        "aws_sdk_mediatailor.types.segmentation_descriptor_list.SegmentationDescriptorList"
    ]
    """<p>The configurations for the SCTE-35 <code>segmentation_descriptor</code> message(s) sent with the <code>time_signal</code> message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSignalMessage) -> dict:
    out: dict = {}
    if "segmentation_descriptors" in value:
        import aws_sdk_mediatailor.types.segmentation_descriptor_list

        out["SegmentationDescriptors"] = (
            aws_sdk_mediatailor.types.segmentation_descriptor_list.serialize_json(
                value["segmentation_descriptors"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimeSignalMessage:
    out: TimeSignalMessage = {}  # type: ignore[typeddict-item]
    if "SegmentationDescriptors" in data:
        import aws_sdk_mediatailor.types.segmentation_descriptor_list

        out["segmentation_descriptors"] = (
            aws_sdk_mediatailor.types.segmentation_descriptor_list.deserialize_json(
                data["SegmentationDescriptors"]
            )
        )
    return out
