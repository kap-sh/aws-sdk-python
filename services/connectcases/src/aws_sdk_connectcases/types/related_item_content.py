"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.connect_case_content
    import aws_sdk_connectcases.types.contact_content
    import aws_sdk_connectcases.types.custom_content
    import aws_sdk_connectcases.types.sla_content
    import aws_sdk_connectcases.types.comment_content
    import aws_sdk_connectcases.types.file_content


class _RelatedItemContent_contact(TypedDict):
    contact: "aws_sdk_connectcases.types.contact_content.ContactContent"


class _RelatedItemContent_comment(TypedDict):
    comment: "aws_sdk_connectcases.types.comment_content.CommentContent"


class _RelatedItemContent_file(TypedDict):
    file: "aws_sdk_connectcases.types.file_content.FileContent"


class _RelatedItemContent_sla(TypedDict):
    sla: "aws_sdk_connectcases.types.sla_content.SlaContent"


class _RelatedItemContent_connectCase(TypedDict):
    connectCase: "aws_sdk_connectcases.types.connect_case_content.ConnectCaseContent"


class _RelatedItemContent_custom(TypedDict):
    custom: "aws_sdk_connectcases.types.custom_content.CustomContent"


RelatedItemContent: TypeAlias = (
    _RelatedItemContent_contact
    | _RelatedItemContent_comment
    | _RelatedItemContent_file
    | _RelatedItemContent_sla
    | _RelatedItemContent_connectCase
    | _RelatedItemContent_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemContent) -> dict:
    if "contact" in value:
        import aws_sdk_connectcases.types.contact_content

        return {
            "contact": aws_sdk_connectcases.types.contact_content.serialize_json(
                value["contact"]
            )
        }
    elif "comment" in value:
        import aws_sdk_connectcases.types.comment_content

        return {
            "comment": aws_sdk_connectcases.types.comment_content.serialize_json(
                value["comment"]
            )
        }
    elif "file" in value:
        import aws_sdk_connectcases.types.file_content

        return {
            "file": aws_sdk_connectcases.types.file_content.serialize_json(
                value["file"]
            )
        }
    elif "sla" in value:
        import aws_sdk_connectcases.types.sla_content

        return {
            "sla": aws_sdk_connectcases.types.sla_content.serialize_json(value["sla"])
        }
    elif "connectCase" in value:
        import aws_sdk_connectcases.types.connect_case_content

        return {
            "connectCase": aws_sdk_connectcases.types.connect_case_content.serialize_json(
                value["connectCase"]
            )
        }
    elif "custom" in value:
        import aws_sdk_connectcases.types.custom_content

        return {
            "custom": aws_sdk_connectcases.types.custom_content.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemContent: no variant present")


def deserialize_json(data: dict) -> RelatedItemContent:
    if "contact" in data:
        import aws_sdk_connectcases.types.contact_content

        return {
            "contact": aws_sdk_connectcases.types.contact_content.deserialize_json(
                data["contact"]
            )
        }
    elif "comment" in data:
        import aws_sdk_connectcases.types.comment_content

        return {
            "comment": aws_sdk_connectcases.types.comment_content.deserialize_json(
                data["comment"]
            )
        }
    elif "file" in data:
        import aws_sdk_connectcases.types.file_content

        return {
            "file": aws_sdk_connectcases.types.file_content.deserialize_json(
                data["file"]
            )
        }
    elif "sla" in data:
        import aws_sdk_connectcases.types.sla_content

        return {
            "sla": aws_sdk_connectcases.types.sla_content.deserialize_json(data["sla"])
        }
    elif "connectCase" in data:
        import aws_sdk_connectcases.types.connect_case_content

        return {
            "connectCase": aws_sdk_connectcases.types.connect_case_content.deserialize_json(
                data["connectCase"]
            )
        }
    elif "custom" in data:
        import aws_sdk_connectcases.types.custom_content

        return {
            "custom": aws_sdk_connectcases.types.custom_content.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError("RelatedItemContent: no recognized variant key")
