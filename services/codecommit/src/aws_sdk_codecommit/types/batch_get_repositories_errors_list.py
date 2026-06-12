"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetRepositoriesErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.batch_get_repositories_error

BatchGetRepositoriesErrorsList: TypeAlias = list[
    "aws_sdk_codecommit.types.batch_get_repositories_error.BatchGetRepositoriesError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetRepositoriesErrorsList) -> list:
    import aws_sdk_codecommit.types.batch_get_repositories_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.batch_get_repositories_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchGetRepositoriesErrorsList:
    import aws_sdk_codecommit.types.batch_get_repositories_error

    out: BatchGetRepositoriesErrorsList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.batch_get_repositories_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
