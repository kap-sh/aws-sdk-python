"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_id

DocumentIdList: TypeAlias = list["aws_sdk_kendra.types.document_id.DocumentId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DocumentIdList:
    return list(data)
