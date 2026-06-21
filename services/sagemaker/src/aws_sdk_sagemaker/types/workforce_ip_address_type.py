"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceIpAddressType``."""

from typing import Literal, TypeAlias, cast

WorkforceIpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkforceIpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkforceIpAddressType:
    return cast(WorkforceIpAddressType, data)
