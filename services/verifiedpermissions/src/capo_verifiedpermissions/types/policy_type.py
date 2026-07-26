"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyType``."""

from typing import Literal, TypeAlias, cast

PolicyType: TypeAlias = Literal[
    "STATIC",
    "TEMPLATE_LINKED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PolicyType:
    return cast(PolicyType, data)
