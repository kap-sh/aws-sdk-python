"""Generated from Smithy shape ``com.amazonaws.firehose#DefaultDocumentIdFormat``."""

from typing import Literal, TypeAlias, cast

DefaultDocumentIdFormat: TypeAlias = Literal[
    "FIREHOSE_DEFAULT",
    "NO_DOCUMENT_ID",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultDocumentIdFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DefaultDocumentIdFormat:
    return cast(DefaultDocumentIdFormat, data)
