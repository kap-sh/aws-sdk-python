"""Generated from Smithy shape ``com.amazonaws.ecr#EnhancedImageScanFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.enhanced_image_scan_finding

EnhancedImageScanFindingList: TypeAlias = list[
    "capo_ecr.types.enhanced_image_scan_finding.EnhancedImageScanFinding"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnhancedImageScanFindingList) -> list:
    import capo_ecr.types.enhanced_image_scan_finding

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.enhanced_image_scan_finding.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnhancedImageScanFindingList:
    import capo_ecr.types.enhanced_image_scan_finding

    out: EnhancedImageScanFindingList = []
    for item in data:
        out.append(
            capo_ecr.types.enhanced_image_scan_finding.deserialize_aws_json_1_1(item)
        )
    return out
