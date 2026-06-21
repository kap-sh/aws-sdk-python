"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSQuotaType``."""

from typing import Literal, TypeAlias, cast

OpenZFSQuotaType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSQuotaType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSQuotaType:
    return cast(OpenZFSQuotaType, data)
