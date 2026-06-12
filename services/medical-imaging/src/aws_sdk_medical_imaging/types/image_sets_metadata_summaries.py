"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetsMetadataSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.image_sets_metadata_summary

ImageSetsMetadataSummaries: TypeAlias = list[
    "aws_sdk_medical_imaging.types.image_sets_metadata_summary.ImageSetsMetadataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetsMetadataSummaries) -> list:
    import aws_sdk_medical_imaging.types.image_sets_metadata_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medical_imaging.types.image_sets_metadata_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ImageSetsMetadataSummaries:
    import aws_sdk_medical_imaging.types.image_sets_metadata_summary

    out: ImageSetsMetadataSummaries = []
    for item in data:
        out.append(
            aws_sdk_medical_imaging.types.image_sets_metadata_summary.deserialize_json(
                item
            )
        )
    return out
