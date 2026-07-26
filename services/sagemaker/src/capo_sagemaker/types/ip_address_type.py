"""Generated from Smithy shape ``com.amazonaws.sagemaker#IPAddressType``."""

from typing import Literal, TypeAlias, cast

IPAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IPAddressType:
    return cast(IPAddressType, data)
