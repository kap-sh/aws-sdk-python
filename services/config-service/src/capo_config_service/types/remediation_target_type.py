"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationTargetType``."""

from typing import Literal, TypeAlias, cast

RemediationTargetType: TypeAlias = Literal["SSM_DOCUMENT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemediationTargetType:
    return cast(RemediationTargetType, data)
