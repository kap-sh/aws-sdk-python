"""Generated from Smithy shape ``com.amazonaws.ecr#EnhancedImageScanFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.enhanced_image_scan_finding

EnhancedImageScanFindingList: TypeAlias = list[
    "aws_sdk_ecr.types.enhanced_image_scan_finding.EnhancedImageScanFinding"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnhancedImageScanFindingList) -> list:
    import aws_sdk_ecr.types.enhanced_image_scan_finding

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.enhanced_image_scan_finding.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnhancedImageScanFindingList:
    import aws_sdk_ecr.types.enhanced_image_scan_finding

    out: EnhancedImageScanFindingList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.enhanced_image_scan_finding.deserialize_aws_json_1_1(item)
        )
    return out
