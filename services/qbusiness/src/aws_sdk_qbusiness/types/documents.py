"""Generated from Smithy shape ``com.amazonaws.qbusiness#Documents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document

Documents: TypeAlias = list["aws_sdk_qbusiness.types.document.Document"]


# --- restJson1 ser/de ---
def serialize_json(value: Documents) -> list:
    import aws_sdk_qbusiness.types.document

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.document.serialize_json(item))
    return out


def deserialize_json(data: list) -> Documents:
    import aws_sdk_qbusiness.types.document

    out: Documents = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.document.deserialize_json(item))
    return out
