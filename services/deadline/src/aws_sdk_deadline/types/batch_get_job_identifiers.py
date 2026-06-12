"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_job_identifier

BatchGetJobIdentifiers: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_job_identifier.BatchGetJobIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobIdentifiers) -> list:
    import aws_sdk_deadline.types.batch_get_job_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.batch_get_job_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetJobIdentifiers:
    import aws_sdk_deadline.types.batch_get_job_identifier

    out: BatchGetJobIdentifiers = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.batch_get_job_identifier.deserialize_json(item)
        )
    return out
