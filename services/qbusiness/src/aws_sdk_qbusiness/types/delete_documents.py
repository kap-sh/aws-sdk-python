"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteDocuments``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.delete_document

DeleteDocuments: TypeAlias = list["aws_sdk_qbusiness.types.delete_document.DeleteDocument"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDocuments) -> list:
    import aws_sdk_qbusiness.types.delete_document
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.delete_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeleteDocuments:
    import aws_sdk_qbusiness.types.delete_document
    out: DeleteDocuments = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.delete_document.deserialize_json(item))
    return out