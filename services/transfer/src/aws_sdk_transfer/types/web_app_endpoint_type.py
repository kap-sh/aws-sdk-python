"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

WebAppEndpointType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "VPC",
    )
)


def serialize_aws_json_1_1(value: WebAppEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebAppEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebAppEndpointType value: {data!r}")
    return cast(WebAppEndpointType, data)
