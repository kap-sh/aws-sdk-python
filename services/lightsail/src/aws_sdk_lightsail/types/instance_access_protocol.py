"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceAccessProtocol``."""

from typing import Literal, TypeAlias, cast

InstanceAccessProtocol: TypeAlias = Literal[
    "ssh",
    "rdp",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAccessProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceAccessProtocol:
    return cast(InstanceAccessProtocol, data)
