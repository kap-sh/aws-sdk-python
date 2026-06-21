"""Generated from Smithy shape ``com.amazonaws.firehose#HECEndpointType``."""

from typing import Literal, TypeAlias, cast

HECEndpointType: TypeAlias = Literal[
    "Raw",
    "Event",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HECEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HECEndpointType:
    return cast(HECEndpointType, data)
