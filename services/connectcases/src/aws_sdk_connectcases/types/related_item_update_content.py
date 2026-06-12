"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemUpdateContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.comment_update_content
    import aws_sdk_connectcases.types.custom_update_content


class _RelatedItemUpdateContent_comment(TypedDict):
    comment: "aws_sdk_connectcases.types.comment_update_content.CommentUpdateContent"


class _RelatedItemUpdateContent_custom(TypedDict):
    custom: "aws_sdk_connectcases.types.custom_update_content.CustomUpdateContent"


RelatedItemUpdateContent: TypeAlias = (
    _RelatedItemUpdateContent_comment | _RelatedItemUpdateContent_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemUpdateContent) -> dict:
    if "comment" in value:
        import aws_sdk_connectcases.types.comment_update_content

        return {
            "comment": aws_sdk_connectcases.types.comment_update_content.serialize_json(
                value["comment"]
            )
        }
    elif "custom" in value:
        import aws_sdk_connectcases.types.custom_update_content

        return {
            "custom": aws_sdk_connectcases.types.custom_update_content.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemUpdateContent: no variant present")


def deserialize_json(data: dict) -> RelatedItemUpdateContent:
    if "comment" in data:
        import aws_sdk_connectcases.types.comment_update_content

        return {
            "comment": aws_sdk_connectcases.types.comment_update_content.deserialize_json(
                data["comment"]
            )
        }
    elif "custom" in data:
        import aws_sdk_connectcases.types.custom_update_content

        return {
            "custom": aws_sdk_connectcases.types.custom_update_content.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError(
            "RelatedItemUpdateContent: no recognized variant key"
        )
