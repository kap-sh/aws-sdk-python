"""Generated from Smithy shape ``com.amazonaws.lambda#EventError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.error_object
    import aws_sdk_lambda.types.truncated


class EventError(TypedDict):
    payload: NotRequired["aws_sdk_lambda.types.error_object.ErrorObject"]
    """<p>The error payload.</p>"""
    truncated: NotRequired["aws_sdk_lambda.types.truncated.Truncated"]
    """<p>Indicates if the error payload was truncated due to size limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventError) -> dict:
    out: dict = {}
    if "payload" in value:
        import aws_sdk_lambda.types.error_object

        out["Payload"] = aws_sdk_lambda.types.error_object.serialize_json(
            value["payload"]
        )
    if "truncated" in value:
        out["Truncated"] = value["truncated"]
    return out


def deserialize_json(data: dict) -> EventError:
    out: EventError = {}  # type: ignore[typeddict-item]
    if "Payload" in data:
        import aws_sdk_lambda.types.error_object

        out["payload"] = aws_sdk_lambda.types.error_object.deserialize_json(
            data["Payload"]
        )
    if "Truncated" in data:
        out["truncated"] = data["Truncated"]
    return out
