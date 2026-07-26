"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_boolean_email_attribute


class _ArchiveBooleanToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.archive_boolean_email_attribute.ArchiveBooleanEmailAttribute"


ArchiveBooleanToEvaluate: TypeAlias = _ArchiveBooleanToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveBooleanToEvaluate) -> dict:
    if "Attribute" in value:
        import capo_mailmanager.types.archive_boolean_email_attribute

        return {
            "Attribute": capo_mailmanager.types.archive_boolean_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("ArchiveBooleanToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveBooleanToEvaluate:
    if "Attribute" in data:
        import capo_mailmanager.types.archive_boolean_email_attribute

        return {
            "Attribute": capo_mailmanager.types.archive_boolean_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError(
            "ArchiveBooleanToEvaluate: no recognized variant key"
        )
