"""Generated from Smithy shape ``com.amazonaws.eventbridge#EndpointState``."""

from typing import Literal, TypeAlias, cast

EndpointState: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointState:
    return cast(EndpointState, data)
