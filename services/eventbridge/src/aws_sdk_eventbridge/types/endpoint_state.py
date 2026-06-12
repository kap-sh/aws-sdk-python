"""Generated from Smithy shape ``com.amazonaws.eventbridge#EndpointState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "UPDATING",
        "DELETING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "DELETE_FAILED",
    )
)


def serialize_aws_json_1_1(value: EndpointState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointState value: {data!r}")
    return cast(EndpointState, data)
