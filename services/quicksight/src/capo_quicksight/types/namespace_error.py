"""Generated from Smithy shape ``com.amazonaws.quicksight#NamespaceError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.namespace_error_type
    import capo_quicksight.types.string


class NamespaceError(TypedDict, closed=True):
    type: NotRequired["capo_quicksight.types.namespace_error_type.NamespaceErrorType"]
    """<p>The error type.</p>"""
    message: NotRequired["capo_quicksight.types.string.String"]
    """<p>The message for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceError) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_quicksight.types.namespace_error_type

        out["Type"] = capo_quicksight.types.namespace_error_type.serialize_json(
            value["type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NamespaceError:
    out: NamespaceError = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_quicksight.types.namespace_error_type

        out["type"] = capo_quicksight.types.namespace_error_type.deserialize_json(
            data["Type"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
