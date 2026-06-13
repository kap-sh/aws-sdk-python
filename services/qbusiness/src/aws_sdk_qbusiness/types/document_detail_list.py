"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_details

DocumentDetailList: TypeAlias = list[
    "aws_sdk_qbusiness.types.document_details.DocumentDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentDetailList) -> list:
    import aws_sdk_qbusiness.types.document_details

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.document_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentDetailList:
    import aws_sdk_qbusiness.types.document_details

    out: DocumentDetailList = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.document_details.deserialize_json(item))
    return out
