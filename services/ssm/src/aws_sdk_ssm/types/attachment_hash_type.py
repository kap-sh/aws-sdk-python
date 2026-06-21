"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentHashType``."""

from typing import Literal, TypeAlias, cast

AttachmentHashType: TypeAlias = Literal["Sha256",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentHashType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttachmentHashType:
    return cast(AttachmentHashType, data)
