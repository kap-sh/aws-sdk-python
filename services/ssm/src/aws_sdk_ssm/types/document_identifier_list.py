"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_identifier

DocumentIdentifierList: TypeAlias = list[
    "aws_sdk_ssm.types.document_identifier.DocumentIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentIdentifierList) -> list:
    import aws_sdk_ssm.types.document_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.document_identifier.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentIdentifierList:
    import aws_sdk_ssm.types.document_identifier

    out: DocumentIdentifierList = []
    for item in data:
        out.append(aws_sdk_ssm.types.document_identifier.deserialize_aws_json_1_1(item))
    return out
