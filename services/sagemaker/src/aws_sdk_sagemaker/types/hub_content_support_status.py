"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentSupportStatus``."""

from typing import Literal, TypeAlias, cast

HubContentSupportStatus: TypeAlias = Literal[
    "Supported",
    "Deprecated",
    "Restricted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentSupportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentSupportStatus:
    return cast(HubContentSupportStatus, data)
