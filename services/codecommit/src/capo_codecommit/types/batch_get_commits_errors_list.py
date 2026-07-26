"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetCommitsErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.batch_get_commits_error

BatchGetCommitsErrorsList: TypeAlias = list[
    "capo_codecommit.types.batch_get_commits_error.BatchGetCommitsError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCommitsErrorsList) -> list:
    import capo_codecommit.types.batch_get_commits_error

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.batch_get_commits_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchGetCommitsErrorsList:
    import capo_codecommit.types.batch_get_commits_error

    out: BatchGetCommitsErrorsList = []
    for item in data:
        out.append(
            capo_codecommit.types.batch_get_commits_error.deserialize_aws_json_1_1(item)
        )
    return out
