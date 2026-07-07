"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveFilterCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_boolean_expression
    import aws_sdk_mailmanager.types.archive_string_expression


class _ArchiveFilterCondition_StringExpression(TypedDict, closed=True):
    StringExpression: (
        "aws_sdk_mailmanager.types.archive_string_expression.ArchiveStringExpression"
    )


class _ArchiveFilterCondition_BooleanExpression(TypedDict, closed=True):
    BooleanExpression: (
        "aws_sdk_mailmanager.types.archive_boolean_expression.ArchiveBooleanExpression"
    )


ArchiveFilterCondition: TypeAlias = (
    _ArchiveFilterCondition_StringExpression | _ArchiveFilterCondition_BooleanExpression
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveFilterCondition) -> dict:
    if "StringExpression" in value:
        import aws_sdk_mailmanager.types.archive_string_expression

        return {
            "StringExpression": aws_sdk_mailmanager.types.archive_string_expression.serialize_aws_json_1_0(
                value["StringExpression"]
            )
        }
    elif "BooleanExpression" in value:
        import aws_sdk_mailmanager.types.archive_boolean_expression

        return {
            "BooleanExpression": aws_sdk_mailmanager.types.archive_boolean_expression.serialize_aws_json_1_0(
                value["BooleanExpression"]
            )
        }
    else:
        raise SerializationError("ArchiveFilterCondition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveFilterCondition:
    if "StringExpression" in data:
        import aws_sdk_mailmanager.types.archive_string_expression

        return {
            "StringExpression": aws_sdk_mailmanager.types.archive_string_expression.deserialize_aws_json_1_0(
                data["StringExpression"]
            )
        }
    elif "BooleanExpression" in data:
        import aws_sdk_mailmanager.types.archive_boolean_expression

        return {
            "BooleanExpression": aws_sdk_mailmanager.types.archive_boolean_expression.deserialize_aws_json_1_0(
                data["BooleanExpression"]
            )
        }
    else:
        raise DeserializationError("ArchiveFilterCondition: no recognized variant key")
