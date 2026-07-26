"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_string_email_attribute


class _ArchiveStringToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.archive_string_email_attribute.ArchiveStringEmailAttribute"


ArchiveStringToEvaluate: TypeAlias = _ArchiveStringToEvaluate_Attribute


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveStringToEvaluate) -> dict:
    if "Attribute" in value:
        import capo_mailmanager.types.archive_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.archive_string_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("ArchiveStringToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveStringToEvaluate:
    if "Attribute" in data:
        import capo_mailmanager.types.archive_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.archive_string_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        raise DeserializationError("ArchiveStringToEvaluate: no recognized variant key")
