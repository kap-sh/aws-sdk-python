"""Generated from Smithy shape ``com.amazonaws.textract#DocumentPages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.document

DocumentPages: TypeAlias = list["aws_sdk_textract.types.document.Document"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentPages) -> list:
    import aws_sdk_textract.types.document

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentPages:
    import aws_sdk_textract.types.document

    out: DocumentPages = []
    for item in data:
        out.append(aws_sdk_textract.types.document.deserialize_aws_json_1_1(item))
    return out
