"""Generated from Smithy shape ``com.amazonaws.gamelift#IpProtocol``."""

from typing import Literal, TypeAlias, cast

IpProtocol: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpProtocol:
    return cast(IpProtocol, data)
