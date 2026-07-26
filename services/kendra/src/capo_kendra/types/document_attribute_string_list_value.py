"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeStringListValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.string

DocumentAttributeStringListValue: TypeAlias = list["capo_kendra.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeStringListValue) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DocumentAttributeStringListValue:
    return list(data)
