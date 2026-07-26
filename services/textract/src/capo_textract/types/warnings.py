"""Generated from Smithy shape ``com.amazonaws.textract#Warnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.warning

Warnings: TypeAlias = list["capo_textract.types.warning.Warning"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Warnings) -> list:
    import capo_textract.types.warning

    out: list = []
    for item in value:
        out.append(capo_textract.types.warning.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Warnings:
    import capo_textract.types.warning

    out: Warnings = []
    for item in data:
        out.append(capo_textract.types.warning.deserialize_aws_json_1_1(item))
    return out
