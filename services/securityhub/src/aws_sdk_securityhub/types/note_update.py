"""Generated from Smithy shape ``com.amazonaws.securityhub#NoteUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class NoteUpdate(TypedDict):
    text: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The updated note text.</p>"""
    updated_by: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The principal that updated the note.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoteUpdate) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> NoteUpdate:
    out: NoteUpdate = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "UpdatedBy" in data:
        out["updated_by"] = data["UpdatedBy"]
    return out
