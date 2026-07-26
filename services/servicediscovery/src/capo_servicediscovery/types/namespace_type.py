"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceType``."""

from typing import Literal, TypeAlias, cast

NamespaceType: TypeAlias = Literal[
    "DNS_PUBLIC",
    "DNS_PRIVATE",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceType:
    return cast(NamespaceType, data)
