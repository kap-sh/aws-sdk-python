"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Messages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_string


class Messages(TypedDict, closed=True):
    errors: NotRequired["capo_mediaconnect.types.__list_of_string.__listOfString"]
    """<p> A list of errors that might have been generated from processes on this flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_mediaconnect.types.__list_of_string

        out["errors"] = capo_mediaconnect.types.__list_of_string.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> Messages:
    out: Messages = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_mediaconnect.types.__list_of_string

        out["errors"] = capo_mediaconnect.types.__list_of_string.deserialize_json(
            data["errors"]
        )
    return out
