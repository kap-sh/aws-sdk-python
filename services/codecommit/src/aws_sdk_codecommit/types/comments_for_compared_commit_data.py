"""Generated from Smithy shape ``com.amazonaws.codecommit#CommentsForComparedCommitData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comments_for_compared_commit

CommentsForComparedCommitData: TypeAlias = list[
    "aws_sdk_codecommit.types.comments_for_compared_commit.CommentsForComparedCommit"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommentsForComparedCommitData) -> list:
    import aws_sdk_codecommit.types.comments_for_compared_commit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.comments_for_compared_commit.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CommentsForComparedCommitData:
    import aws_sdk_codecommit.types.comments_for_compared_commit

    out: CommentsForComparedCommitData = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.comments_for_compared_commit.deserialize_aws_json_1_1(
                item
            )
        )
    return out
