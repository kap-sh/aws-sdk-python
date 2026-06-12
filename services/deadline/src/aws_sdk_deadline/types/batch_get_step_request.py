"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_step_identifiers


class BatchGetStepRequest(TypedDict):
    identifiers: (
        "aws_sdk_deadline.types.batch_get_step_identifiers.BatchGetStepIdentifiers"
    )
    """<p>The list of step identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_step_identifiers

    out["identifiers"] = (
        aws_sdk_deadline.types.batch_get_step_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetStepRequest:
    out: BatchGetStepRequest = {}  # type: ignore[typeddict-item]
    if "identifiers" in data:
        import aws_sdk_deadline.types.batch_get_step_identifiers

        out["identifiers"] = (
            aws_sdk_deadline.types.batch_get_step_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        raise DeserializationError("BatchGetStepRequest.identifiers required")
    return out
