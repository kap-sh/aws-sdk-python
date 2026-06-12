"""Generated from Smithy shape ``com.amazonaws.inspector#ExclusionPreviewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.exclusion_preview

ExclusionPreviewList: TypeAlias = list[
    "aws_sdk_inspector.types.exclusion_preview.ExclusionPreview"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExclusionPreviewList) -> list:
    import aws_sdk_inspector.types.exclusion_preview

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.exclusion_preview.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExclusionPreviewList:
    import aws_sdk_inspector.types.exclusion_preview

    out: ExclusionPreviewList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.exclusion_preview.deserialize_aws_json_1_1(item)
        )
    return out
