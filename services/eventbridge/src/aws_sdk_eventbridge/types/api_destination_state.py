"""Generated from Smithy shape ``com.amazonaws.eventbridge#ApiDestinationState``."""

from typing import Literal, TypeAlias, cast

ApiDestinationState: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApiDestinationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApiDestinationState:
    return cast(ApiDestinationState, data)
