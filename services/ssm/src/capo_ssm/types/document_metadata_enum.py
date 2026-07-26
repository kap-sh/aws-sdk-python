"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentMetadataEnum``."""

from typing import Literal, TypeAlias, cast

DocumentMetadataEnum: TypeAlias = Literal["DocumentReviews",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadataEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentMetadataEnum:
    return cast(DocumentMetadataEnum, data)
