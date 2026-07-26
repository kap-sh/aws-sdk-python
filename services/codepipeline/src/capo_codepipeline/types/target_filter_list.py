"""Generated from Smithy shape ``com.amazonaws.codepipeline#TargetFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.target_filter

TargetFilterList: TypeAlias = list["capo_codepipeline.types.target_filter.TargetFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFilterList) -> list:
    import capo_codepipeline.types.target_filter

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.target_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetFilterList:
    import capo_codepipeline.types.target_filter

    out: TargetFilterList = []
    for item in data:
        out.append(capo_codepipeline.types.target_filter.deserialize_aws_json_1_1(item))
    return out
