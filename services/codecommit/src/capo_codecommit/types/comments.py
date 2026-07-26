"""Generated from Smithy shape ``com.amazonaws.codecommit#Comments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.comment

Comments: TypeAlias = list["capo_codecommit.types.comment.Comment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Comments) -> list:
    import capo_codecommit.types.comment

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.comment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Comments:
    import capo_codecommit.types.comment

    out: Comments = []
    for item in data:
        out.append(capo_codecommit.types.comment.deserialize_aws_json_1_1(item))
    return out
