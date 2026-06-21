"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentPermissionType``."""

from typing import Literal, TypeAlias, cast

DocumentPermissionType: TypeAlias = Literal["Share",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentPermissionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentPermissionType:
    return cast(DocumentPermissionType, data)
