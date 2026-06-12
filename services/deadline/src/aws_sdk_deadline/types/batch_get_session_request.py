"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_identifiers


class BatchGetSessionRequest(TypedDict):
    identifiers: "aws_sdk_deadline.types.batch_get_session_identifiers.BatchGetSessionIdentifiers"
    """<p>The list of session identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_session_identifiers

    out["identifiers"] = (
        aws_sdk_deadline.types.batch_get_session_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSessionRequest:
    out: BatchGetSessionRequest = {}  # type: ignore[typeddict-item]
    if "identifiers" in data:
        import aws_sdk_deadline.types.batch_get_session_identifiers

        out["identifiers"] = (
            aws_sdk_deadline.types.batch_get_session_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        raise DeserializationError("BatchGetSessionRequest.identifiers required")
    return out
