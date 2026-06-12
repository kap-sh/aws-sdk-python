"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_session_action_errors
    import aws_sdk_deadline.types.batch_get_session_action_items


class BatchGetSessionActionResponse(TypedDict):
    session_actions: "aws_sdk_deadline.types.batch_get_session_action_items.BatchGetSessionActionItems"
    """<p>A list of session actions that were successfully retrieved.</p>"""
    errors: "aws_sdk_deadline.types.batch_get_session_action_errors.BatchGetSessionActionErrors"
    """<p>A list of errors for session actions that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_session_action_items

    out["sessionActions"] = (
        aws_sdk_deadline.types.batch_get_session_action_items.serialize_json(
            value["session_actions"]
        )
    )
    import aws_sdk_deadline.types.batch_get_session_action_errors

    out["errors"] = (
        aws_sdk_deadline.types.batch_get_session_action_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSessionActionResponse:
    out: BatchGetSessionActionResponse = {}  # type: ignore[typeddict-item]
    if "sessionActions" in data:
        import aws_sdk_deadline.types.batch_get_session_action_items

        out["session_actions"] = (
            aws_sdk_deadline.types.batch_get_session_action_items.deserialize_json(
                data["sessionActions"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetSessionActionResponse.session_actions required"
        )
    if "errors" in data:
        import aws_sdk_deadline.types.batch_get_session_action_errors

        out["errors"] = (
            aws_sdk_deadline.types.batch_get_session_action_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetSessionActionResponse.errors required")
    return out
