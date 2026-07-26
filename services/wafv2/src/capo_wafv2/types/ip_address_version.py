"""Generated from Smithy shape ``com.amazonaws.wafv2#IPAddressVersion``."""

from typing import Literal, TypeAlias, cast

IPAddressVersion: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPAddressVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IPAddressVersion:
    return cast(IPAddressVersion, data)
