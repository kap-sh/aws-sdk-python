"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestType``."""

from typing import Literal, TypeAlias, cast

RequestType: TypeAlias = Literal["AutomaticManagement",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RequestType:
    return cast(RequestType, data)
