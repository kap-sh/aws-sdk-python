"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseContentProvider``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_wisdom.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.quick_response_content


class _QuickResponseContentProvider_content(TypedDict):
    content: "aws_sdk_wisdom.types.quick_response_content.QuickResponseContent"


QuickResponseContentProvider: TypeAlias = _QuickResponseContentProvider_content


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseContentProvider) -> dict:
    if "content" in value:
        return {"content": value["content"]}
    else:
        raise SerializationError("QuickResponseContentProvider: no variant present")


def deserialize_json(data: dict) -> QuickResponseContentProvider:
    if "content" in data:
        return {"content": data["content"]}
    else:
        raise DeserializationError(
            "QuickResponseContentProvider: no recognized variant key"
        )
