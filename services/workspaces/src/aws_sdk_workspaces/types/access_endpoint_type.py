"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessEndpointType``."""

from typing import Literal, TypeAlias, cast

AccessEndpointType: TypeAlias = Literal["STREAMING_WSP",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessEndpointType:
    return cast(AccessEndpointType, data)
