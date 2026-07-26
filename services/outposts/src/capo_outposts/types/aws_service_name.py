"""Generated from Smithy shape ``com.amazonaws.outposts#AWSServiceName``."""

from typing import Literal, TypeAlias, cast

AWSServiceName: TypeAlias = Literal[
    "AWS",
    "EC2",
    "ELASTICACHE",
    "ELB",
    "RDS",
    "ROUTE53",
]


# --- restJson1 ser/de ---
def serialize_json(value: AWSServiceName) -> str:
    return value


def deserialize_json(data: str) -> AWSServiceName:
    return cast(AWSServiceName, data)
