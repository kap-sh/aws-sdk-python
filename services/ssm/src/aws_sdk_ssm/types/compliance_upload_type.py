"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceUploadType``."""

from typing import Literal, TypeAlias, cast

ComplianceUploadType: TypeAlias = Literal[
    "COMPLETE",
    "PARTIAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceUploadType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceUploadType:
    return cast(ComplianceUploadType, data)
