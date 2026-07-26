"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateBodyContentProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_unlimited_string


class _MessageTemplateBodyContentProvider_content(TypedDict, closed=True):
    content: "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"


MessageTemplateBodyContentProvider: TypeAlias = (
    _MessageTemplateBodyContentProvider_content
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateBodyContentProvider) -> dict:
    if "content" in value:
        return {"content": value["content"]}
    else:
        raise SerializationError(
            "MessageTemplateBodyContentProvider: no variant present"
        )


def deserialize_json(data: dict) -> MessageTemplateBodyContentProvider:
    if "content" in data:
        return {"content": data["content"]}
    else:
        raise DeserializationError(
            "MessageTemplateBodyContentProvider: no recognized variant key"
        )
