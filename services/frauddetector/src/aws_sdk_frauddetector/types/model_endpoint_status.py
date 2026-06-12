"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

ModelEndpointStatus: TypeAlias = Literal[
    "ASSOCIATED",
    "DISSOCIATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATED",
        "DISSOCIATED",
    )
)


def serialize_aws_json_1_1(value: ModelEndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelEndpointStatus value: {data!r}")
    return cast(ModelEndpointStatus, data)
