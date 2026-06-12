"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_action_identifiers


class BatchGetSessionActionRequest(TypedDict):
    identifiers: "aws_sdk_deadline.types.batch_get_session_action_identifiers.BatchGetSessionActionIdentifiers"
    """<p>The list of session action identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_session_action_identifiers

    out["identifiers"] = (
        aws_sdk_deadline.types.batch_get_session_action_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSessionActionRequest:
    out: BatchGetSessionActionRequest = {}  # type: ignore[typeddict-item]
    if "identifiers" in data:
        import aws_sdk_deadline.types.batch_get_session_action_identifiers

        out["identifiers"] = (
            aws_sdk_deadline.types.batch_get_session_action_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        raise DeserializationError("BatchGetSessionActionRequest.identifiers required")
    return out
