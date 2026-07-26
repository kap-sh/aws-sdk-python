"""Generated from Smithy shape ``com.amazonaws.route53resolver#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal[
    "DoH",
    "Do53",
    "DoH-FIPS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Protocol:
    return cast(Protocol, data)
