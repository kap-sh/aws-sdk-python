"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_boolean_email_attribute


class _ArchiveBooleanToEvaluate_Attribute(TypedDict):
    Attribute: "aws_sdk_mailmanager.types.archive_boolean_email_attribute.ArchiveBooleanEmailAttribute"


ArchiveBooleanToEvaluate: TypeAlias = _ArchiveBooleanToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveBooleanToEvaluate) -> dict:
    if "Attribute" in value:
        import aws_sdk_mailmanager.types.archive_boolean_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.archive_boolean_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("ArchiveBooleanToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveBooleanToEvaluate:
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.archive_boolean_email_attribute

        return {
            "Attribute": aws_sdk_mailmanager.types.archive_boolean_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError(
            "ArchiveBooleanToEvaluate: no recognized variant key"
        )
