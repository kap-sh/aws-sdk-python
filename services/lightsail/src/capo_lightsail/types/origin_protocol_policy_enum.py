"""Generated from Smithy shape ``com.amazonaws.lightsail#OriginProtocolPolicyEnum``."""

from typing import Literal, TypeAlias, cast

OriginProtocolPolicyEnum: TypeAlias = Literal[
    "http-only",
    "https-only",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OriginProtocolPolicyEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginProtocolPolicyEnum:
    return cast(OriginProtocolPolicyEnum, data)
