"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemInputContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.comment_content
    import aws_sdk_connectcases.types.connect_case_input_content
    import aws_sdk_connectcases.types.contact
    import aws_sdk_connectcases.types.custom_input_content
    import aws_sdk_connectcases.types.file_content
    import aws_sdk_connectcases.types.sla_input_content


class _RelatedItemInputContent_contact(TypedDict, closed=True):
    contact: "aws_sdk_connectcases.types.contact.Contact"


class _RelatedItemInputContent_comment(TypedDict, closed=True):
    comment: "aws_sdk_connectcases.types.comment_content.CommentContent"


class _RelatedItemInputContent_file(TypedDict, closed=True):
    file: "aws_sdk_connectcases.types.file_content.FileContent"


class _RelatedItemInputContent_sla(TypedDict, closed=True):
    sla: "aws_sdk_connectcases.types.sla_input_content.SlaInputContent"


class _RelatedItemInputContent_connectCase(TypedDict, closed=True):
    connectCase: (
        "aws_sdk_connectcases.types.connect_case_input_content.ConnectCaseInputContent"
    )


class _RelatedItemInputContent_custom(TypedDict, closed=True):
    custom: "aws_sdk_connectcases.types.custom_input_content.CustomInputContent"


RelatedItemInputContent: TypeAlias = (
    _RelatedItemInputContent_contact
    | _RelatedItemInputContent_comment
    | _RelatedItemInputContent_file
    | _RelatedItemInputContent_sla
    | _RelatedItemInputContent_connectCase
    | _RelatedItemInputContent_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemInputContent) -> dict:
    if "contact" in value:
        import aws_sdk_connectcases.types.contact

        return {
            "contact": aws_sdk_connectcases.types.contact.serialize_json(
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
        import aws_sdk_connectcases.types.sla_input_content

        return {
            "sla": aws_sdk_connectcases.types.sla_input_content.serialize_json(
                value["sla"]
            )
        }
    elif "connectCase" in value:
        import aws_sdk_connectcases.types.connect_case_input_content

        return {
            "connectCase": aws_sdk_connectcases.types.connect_case_input_content.serialize_json(
                value["connectCase"]
            )
        }
    elif "custom" in value:
        import aws_sdk_connectcases.types.custom_input_content

        return {
            "custom": aws_sdk_connectcases.types.custom_input_content.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemInputContent: no variant present")


def deserialize_json(data: dict) -> RelatedItemInputContent:
    if "contact" in data:
        import aws_sdk_connectcases.types.contact

        return {
            "contact": aws_sdk_connectcases.types.contact.deserialize_json(
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
        import aws_sdk_connectcases.types.sla_input_content

        return {
            "sla": aws_sdk_connectcases.types.sla_input_content.deserialize_json(
                data["sla"]
            )
        }
    elif "connectCase" in data:
        import aws_sdk_connectcases.types.connect_case_input_content

        return {
            "connectCase": aws_sdk_connectcases.types.connect_case_input_content.deserialize_json(
                data["connectCase"]
            )
        }
    elif "custom" in data:
        import aws_sdk_connectcases.types.custom_input_content

        return {
            "custom": aws_sdk_connectcases.types.custom_input_content.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError("RelatedItemInputContent: no recognized variant key")
