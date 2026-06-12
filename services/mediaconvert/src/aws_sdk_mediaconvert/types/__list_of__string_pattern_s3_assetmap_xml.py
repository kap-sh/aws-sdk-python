"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__stringPatternS3ASSETMAPXml``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_pattern_s3_assetmap_xml

__listOf__stringPatternS3ASSETMAPXml: TypeAlias = list[
    "aws_sdk_mediaconvert.types.__string_pattern_s3_assetmap_xml.__stringPatternS3ASSETMAPXml"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringPatternS3ASSETMAPXml) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringPatternS3ASSETMAPXml:
    return list(data)
