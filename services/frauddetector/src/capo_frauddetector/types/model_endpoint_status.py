"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelEndpointStatus``."""

from typing import Literal, TypeAlias, cast

ModelEndpointStatus: TypeAlias = Literal[
    "ASSOCIATED",
    "DISSOCIATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelEndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelEndpointStatus:
    return cast(ModelEndpointStatus, data)
