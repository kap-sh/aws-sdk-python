"""Generated from Smithy shape ``com.amazonaws.emr#LogUploadPolicyValue``."""

from typing import Literal, TypeAlias, cast

LogUploadPolicyValue: TypeAlias = Literal[
    "emr-managed",
    "on-customer-s3only",
    "disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogUploadPolicyValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogUploadPolicyValue:
    return cast(LogUploadPolicyValue, data)
