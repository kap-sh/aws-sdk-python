"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_job_identifiers


class BatchGetJobRequest(TypedDict, closed=True):
    identifiers: (
        "aws_sdk_deadline.types.batch_get_job_identifiers.BatchGetJobIdentifiers"
    )
    """<p>The list of job identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_job_identifiers

    out["identifiers"] = (
        aws_sdk_deadline.types.batch_get_job_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetJobRequest:
    out: BatchGetJobRequest = {}  # type: ignore[typeddict-item]
    if "identifiers" in data:
        import aws_sdk_deadline.types.batch_get_job_identifiers

        out["identifiers"] = (
            aws_sdk_deadline.types.batch_get_job_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        raise DeserializationError("BatchGetJobRequest.identifiers required")
    return out
