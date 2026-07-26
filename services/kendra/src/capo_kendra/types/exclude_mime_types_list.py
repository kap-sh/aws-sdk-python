"""Generated from Smithy shape ``com.amazonaws.kendra#ExcludeMimeTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.mime_type

ExcludeMimeTypesList: TypeAlias = list["capo_kendra.types.mime_type.MimeType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludeMimeTypesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludeMimeTypesList:
    return list(data)
