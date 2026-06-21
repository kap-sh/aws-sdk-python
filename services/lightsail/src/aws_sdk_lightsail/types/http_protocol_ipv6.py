"""Generated from Smithy shape ``com.amazonaws.lightsail#HttpProtocolIpv6``."""

from typing import Literal, TypeAlias, cast

HttpProtocolIpv6: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpProtocolIpv6) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HttpProtocolIpv6:
    return cast(HttpProtocolIpv6, data)
