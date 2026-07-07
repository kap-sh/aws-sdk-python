"""Generated from Smithy shape ``com.amazonaws.medialive#AvailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.avail_settings
    import aws_sdk_medialive.types.scte35_segmentation_scope


class AvailConfiguration(TypedDict, closed=True):
    avail_settings: NotRequired["aws_sdk_medialive.types.avail_settings.AvailSettings"]
    """Controls how SCTE-35 messages create cues. Splice Insert mode treats all segmentation signals traditionally. With Time Signal APOS mode only Time Signal Placement Opportunity and Break messages create segment breaks. With ESAM mode, signals are forwarded to an ESAM server for possible update."""
    scte35_segmentation_scope: NotRequired[
        "aws_sdk_medialive.types.scte35_segmentation_scope.Scte35SegmentationScope"
    ]
    """Configures whether SCTE 35 passthrough triggers segment breaks in all output groups that use segmented outputs. Insertion of a SCTE 35 message typically results in a segment break, in addition to the regular cadence of breaks. The segment breaks appear in video outputs, audio outputs, and captions outputs (if any). ALL_OUTPUT_GROUPS: Default. Insert the segment break in in all output groups that have segmented outputs. This is the legacy behavior. SCTE35_ENABLED_OUTPUT_GROUPS: Insert the segment break only in output groups that have SCTE 35 passthrough enabled. This is the recommended value, because it reduces unnecessary segment breaks."""


# --- restJson1 ser/de ---
def serialize_json(value: AvailConfiguration) -> dict:
    out: dict = {}
    if "avail_settings" in value:
        import aws_sdk_medialive.types.avail_settings

        out["availSettings"] = aws_sdk_medialive.types.avail_settings.serialize_json(
            value["avail_settings"]
        )
    if "scte35_segmentation_scope" in value:
        import aws_sdk_medialive.types.scte35_segmentation_scope

        out["scte35SegmentationScope"] = (
            aws_sdk_medialive.types.scte35_segmentation_scope.serialize_json(
                value["scte35_segmentation_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> AvailConfiguration:
    out: AvailConfiguration = {}  # type: ignore[typeddict-item]
    if "availSettings" in data:
        import aws_sdk_medialive.types.avail_settings

        out["avail_settings"] = aws_sdk_medialive.types.avail_settings.deserialize_json(
            data["availSettings"]
        )
    if "scte35SegmentationScope" in data:
        import aws_sdk_medialive.types.scte35_segmentation_scope

        out["scte35_segmentation_scope"] = (
            aws_sdk_medialive.types.scte35_segmentation_scope.deserialize_json(
                data["scte35SegmentationScope"]
            )
        )
    return out
