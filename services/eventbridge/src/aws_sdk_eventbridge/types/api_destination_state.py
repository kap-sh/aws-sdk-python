"""Generated from Smithy shape ``com.amazonaws.eventbridge#ApiDestinationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

ApiDestinationState: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: ApiDestinationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApiDestinationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiDestinationState value: {data!r}")
    return cast(ApiDestinationState, data)
