"""Generated from Smithy shape ``com.amazonaws.ecr#ImageScanFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image_scan_finding

ImageScanFindingList: TypeAlias = list[
    "capo_ecr.types.image_scan_finding.ImageScanFinding"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageScanFindingList) -> list:
    import capo_ecr.types.image_scan_finding

    out: list = []
    for item in value:
        out.append(capo_ecr.types.image_scan_finding.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageScanFindingList:
    import capo_ecr.types.image_scan_finding

    out: ImageScanFindingList = []
    for item in data:
        out.append(capo_ecr.types.image_scan_finding.deserialize_aws_json_1_1(item))
    return out
