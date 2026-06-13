"""Generated from Smithy shape ``com.amazonaws.securityagent#DocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.document_info

DocumentList: TypeAlias = list["aws_sdk_securityagent.types.document_info.DocumentInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentList) -> list:
    import aws_sdk_securityagent.types.document_info

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.document_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentList:
    import aws_sdk_securityagent.types.document_info

    out: DocumentList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.document_info.deserialize_json(item))
    return out
