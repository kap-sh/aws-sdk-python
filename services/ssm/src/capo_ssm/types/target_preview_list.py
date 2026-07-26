"""Generated from Smithy shape ``com.amazonaws.ssm#TargetPreviewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.target_preview

TargetPreviewList: TypeAlias = list["capo_ssm.types.target_preview.TargetPreview"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetPreviewList) -> list:
    import capo_ssm.types.target_preview

    out: list = []
    for item in value:
        out.append(capo_ssm.types.target_preview.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetPreviewList:
    import capo_ssm.types.target_preview

    out: TargetPreviewList = []
    for item in data:
        out.append(capo_ssm.types.target_preview.deserialize_aws_json_1_1(item))
    return out
