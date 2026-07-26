"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_scan_finding

ImageScanFindingsList: TypeAlias = list[
    "capo_imagebuilder.types.image_scan_finding.ImageScanFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFindingsList) -> list:
    import capo_imagebuilder.types.image_scan_finding

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.image_scan_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageScanFindingsList:
    import capo_imagebuilder.types.image_scan_finding

    out: ImageScanFindingsList = []
    for item in data:
        out.append(capo_imagebuilder.types.image_scan_finding.deserialize_json(item))
    return out
