"""Generated from Smithy shape ``com.amazonaws.transfer#EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

EndpointType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
    "VPC_ENDPOINT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "VPC",
        "VPC_ENDPOINT",
    )
)


def serialize_aws_json_1_1(value: EndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
