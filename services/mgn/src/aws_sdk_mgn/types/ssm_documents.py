"""Generated from Smithy shape ``com.amazonaws.mgn#SsmDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.ssm_document

SsmDocuments: TypeAlias = list["aws_sdk_mgn.types.ssm_document.SsmDocument"]


# --- restJson1 ser/de ---
def serialize_json(value: SsmDocuments) -> list:
    import aws_sdk_mgn.types.ssm_document

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.ssm_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> SsmDocuments:
    import aws_sdk_mgn.types.ssm_document

    out: SsmDocuments = []
    for item in data:
        out.append(aws_sdk_mgn.types.ssm_document.deserialize_json(item))
    return out
