"""Generated from Smithy shape ``com.amazonaws.inspector#ExclusionPreviewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.exclusion_preview

ExclusionPreviewList: TypeAlias = list[
    "capo_inspector.types.exclusion_preview.ExclusionPreview"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExclusionPreviewList) -> list:
    import capo_inspector.types.exclusion_preview

    out: list = []
    for item in value:
        out.append(capo_inspector.types.exclusion_preview.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExclusionPreviewList:
    import capo_inspector.types.exclusion_preview

    out: ExclusionPreviewList = []
    for item in data:
        out.append(
            capo_inspector.types.exclusion_preview.deserialize_aws_json_1_1(item)
        )
    return out
