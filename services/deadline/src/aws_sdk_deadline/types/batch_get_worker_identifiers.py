"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_worker_identifier

BatchGetWorkerIdentifiers: TypeAlias = list[
    "aws_sdk_deadline.types.batch_get_worker_identifier.BatchGetWorkerIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerIdentifiers) -> list:
    import aws_sdk_deadline.types.batch_get_worker_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.batch_get_worker_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetWorkerIdentifiers:
    import aws_sdk_deadline.types.batch_get_worker_identifier

    out: BatchGetWorkerIdentifiers = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.batch_get_worker_identifier.deserialize_json(item)
        )
    return out
