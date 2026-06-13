"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Messages``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_string


class Messages(TypedDict):
    errors: NotRequired["aws_sdk_mediaconnect.types.__list_of_string.__listOfString"]
    """<p> A list of errors that might have been generated from processes on this flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["errors"] = aws_sdk_mediaconnect.types.__list_of_string.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> Messages:
    out: Messages = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_mediaconnect.types.__list_of_string

        out["errors"] = aws_sdk_mediaconnect.types.__list_of_string.deserialize_json(
            data["errors"]
        )
    return out
