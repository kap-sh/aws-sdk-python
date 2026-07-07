"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35Descriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.scte35_descriptor_settings


class Scte35Descriptor(TypedDict, closed=True):
    scte35_descriptor_settings: NotRequired[
        "aws_sdk_medialive.types.scte35_descriptor_settings.Scte35DescriptorSettings"
    ]
    """SCTE-35 Descriptor Settings."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35Descriptor) -> dict:
    out: dict = {}
    if "scte35_descriptor_settings" in value:
        import aws_sdk_medialive.types.scte35_descriptor_settings

        out["scte35DescriptorSettings"] = (
            aws_sdk_medialive.types.scte35_descriptor_settings.serialize_json(
                value["scte35_descriptor_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Scte35Descriptor:
    out: Scte35Descriptor = {}  # type: ignore[typeddict-item]
    if "scte35DescriptorSettings" in data:
        import aws_sdk_medialive.types.scte35_descriptor_settings

        out["scte35_descriptor_settings"] = (
            aws_sdk_medialive.types.scte35_descriptor_settings.deserialize_json(
                data["scte35DescriptorSettings"]
            )
        )
    return out
