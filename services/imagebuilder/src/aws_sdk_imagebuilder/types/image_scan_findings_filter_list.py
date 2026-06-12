"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFindingsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_scan_findings_filter

ImageScanFindingsFilterList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.image_scan_findings_filter.ImageScanFindingsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFindingsFilterList) -> list:
    import aws_sdk_imagebuilder.types.image_scan_findings_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.image_scan_findings_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ImageScanFindingsFilterList:
    import aws_sdk_imagebuilder.types.image_scan_findings_filter

    out: ImageScanFindingsFilterList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.image_scan_findings_filter.deserialize_json(item)
        )
    return out
