"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentRequiresList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.document_requires

DocumentRequiresList: TypeAlias = list[
    "capo_ssm.types.document_requires.DocumentRequires"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentRequiresList) -> list:
    import capo_ssm.types.document_requires

    out: list = []
    for item in value:
        out.append(capo_ssm.types.document_requires.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentRequiresList:
    import capo_ssm.types.document_requires

    out: DocumentRequiresList = []
    for item in data:
        out.append(capo_ssm.types.document_requires.deserialize_aws_json_1_1(item))
    return out
