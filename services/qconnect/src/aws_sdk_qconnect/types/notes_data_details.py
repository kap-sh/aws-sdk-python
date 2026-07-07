"""Generated from Smithy shape ``com.amazonaws.qconnect#NotesDataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_sensitive_string


class NotesDataDetails(TypedDict, closed=True):
    completion: NotRequired[
        "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>The completion data for notes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotesDataDetails) -> dict:
    out: dict = {}
    if "completion" in value:
        out["completion"] = value["completion"]
    return out


def deserialize_json(data: dict) -> NotesDataDetails:
    out: NotesDataDetails = {}  # type: ignore[typeddict-item]
    if "completion" in data:
        out["completion"] = data["completion"]
    return out
