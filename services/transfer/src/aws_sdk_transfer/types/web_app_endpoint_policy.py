"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppEndpointPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

WebAppEndpointPolicy: TypeAlias = Literal[
    "FIPS",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIPS",
        "STANDARD",
    )
)


def serialize_aws_json_1_1(value: WebAppEndpointPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebAppEndpointPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebAppEndpointPolicy value: {data!r}")
    return cast(WebAppEndpointPolicy, data)
