"""Generated from Smithy shape ``com.amazonaws.odb#VpcEndpointType``."""

from typing import Literal, TypeAlias, cast

VpcEndpointType: TypeAlias = Literal["SERVICENETWORK",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VpcEndpointType:
    return cast(VpcEndpointType, data)
