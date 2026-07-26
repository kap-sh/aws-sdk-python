"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeHunks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.merge_hunk

MergeHunks: TypeAlias = list["capo_codecommit.types.merge_hunk.MergeHunk"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeHunks) -> list:
    import capo_codecommit.types.merge_hunk

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.merge_hunk.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MergeHunks:
    import capo_codecommit.types.merge_hunk

    out: MergeHunks = []
    for item in data:
        out.append(capo_codecommit.types.merge_hunk.deserialize_aws_json_1_1(item))
    return out
