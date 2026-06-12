"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_worker_identifiers


class BatchGetWorkerRequest(TypedDict):
    identifiers: (
        "aws_sdk_deadline.types.batch_get_worker_identifiers.BatchGetWorkerIdentifiers"
    )
    """<p>The list of worker identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_worker_identifiers

    out["identifiers"] = (
        aws_sdk_deadline.types.batch_get_worker_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetWorkerRequest:
    out: BatchGetWorkerRequest = {}  # type: ignore[typeddict-item]
    if "identifiers" in data:
        import aws_sdk_deadline.types.batch_get_worker_identifiers

        out["identifiers"] = (
            aws_sdk_deadline.types.batch_get_worker_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        raise DeserializationError("BatchGetWorkerRequest.identifiers required")
    return out
