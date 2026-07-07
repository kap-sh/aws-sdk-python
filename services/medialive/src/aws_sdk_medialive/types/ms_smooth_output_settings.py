"""Generated from Smithy shape ``com.amazonaws.medialive#MsSmoothOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.ms_smooth_h265_packaging_type


class MsSmoothOutputSettings(TypedDict, closed=True):
    h265_packaging_type: NotRequired[
        "aws_sdk_medialive.types.ms_smooth_h265_packaging_type.MsSmoothH265PackagingType"
    ]
    """Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1."""
    name_modifier: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """String concatenated to the end of the destination filename. Required for multiple outputs of the same type."""


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothOutputSettings) -> dict:
    out: dict = {}
    if "h265_packaging_type" in value:
        import aws_sdk_medialive.types.ms_smooth_h265_packaging_type

        out["h265PackagingType"] = (
            aws_sdk_medialive.types.ms_smooth_h265_packaging_type.serialize_json(
                value["h265_packaging_type"]
            )
        )
    if "name_modifier" in value:
        out["nameModifier"] = value["name_modifier"]
    return out


def deserialize_json(data: dict) -> MsSmoothOutputSettings:
    out: MsSmoothOutputSettings = {}  # type: ignore[typeddict-item]
    if "h265PackagingType" in data:
        import aws_sdk_medialive.types.ms_smooth_h265_packaging_type

        out["h265_packaging_type"] = (
            aws_sdk_medialive.types.ms_smooth_h265_packaging_type.deserialize_json(
                data["h265PackagingType"]
            )
        )
    if "nameModifier" in data:
        out["name_modifier"] = data["nameModifier"]
    return out
