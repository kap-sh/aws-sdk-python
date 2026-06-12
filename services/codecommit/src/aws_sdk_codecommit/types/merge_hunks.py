"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeHunks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.merge_hunk

MergeHunks: TypeAlias = list["aws_sdk_codecommit.types.merge_hunk.MergeHunk"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeHunks) -> list:
    import aws_sdk_codecommit.types.merge_hunk

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.merge_hunk.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MergeHunks:
    import aws_sdk_codecommit.types.merge_hunk

    out: MergeHunks = []
    for item in data:
        out.append(aws_sdk_codecommit.types.merge_hunk.deserialize_aws_json_1_1(item))
    return out
