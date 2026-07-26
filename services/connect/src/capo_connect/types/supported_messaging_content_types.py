"""Generated from Smithy shape ``com.amazonaws.connect#SupportedMessagingContentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.supported_messaging_content_type

SupportedMessagingContentTypes: TypeAlias = list[
    "capo_connect.types.supported_messaging_content_type.SupportedMessagingContentType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedMessagingContentTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> SupportedMessagingContentTypes:
    return list(data)
