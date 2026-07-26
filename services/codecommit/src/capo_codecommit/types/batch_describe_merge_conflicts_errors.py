"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDescribeMergeConflictsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.batch_describe_merge_conflicts_error

BatchDescribeMergeConflictsErrors: TypeAlias = list[
    "capo_codecommit.types.batch_describe_merge_conflicts_error.BatchDescribeMergeConflictsError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeMergeConflictsErrors) -> list:
    import capo_codecommit.types.batch_describe_merge_conflicts_error

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.batch_describe_merge_conflicts_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDescribeMergeConflictsErrors:
    import capo_codecommit.types.batch_describe_merge_conflicts_error

    out: BatchDescribeMergeConflictsErrors = []
    for item in data:
        out.append(
            capo_codecommit.types.batch_describe_merge_conflicts_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
