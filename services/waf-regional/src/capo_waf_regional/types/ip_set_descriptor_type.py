"""Generated from Smithy shape ``com.amazonaws.wafregional#IPSetDescriptorType``."""

from typing import Literal, TypeAlias, cast

IPSetDescriptorType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetDescriptorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IPSetDescriptorType:
    return cast(IPSetDescriptorType, data)
