"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentHashType``."""

from typing import Literal, TypeAlias, cast

DocumentHashType: TypeAlias = Literal[
    "Sha256",
    "Sha1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentHashType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentHashType:
    return cast(DocumentHashType, data)
