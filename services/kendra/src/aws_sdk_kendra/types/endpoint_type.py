"""Generated from Smithy shape ``com.amazonaws.kendra#EndpointType``."""

from typing import Literal, TypeAlias, cast

EndpointType: TypeAlias = Literal["HOME",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointType:
    return cast(EndpointType, data)
