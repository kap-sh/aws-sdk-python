"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppVpcEndpointIpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

WebAppVpcEndpointIpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUALSTACK",
    )
)


def serialize_aws_json_1_1(value: WebAppVpcEndpointIpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebAppVpcEndpointIpAddressType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WebAppVpcEndpointIpAddressType value: {data!r}"
        )
    return cast(WebAppVpcEndpointIpAddressType, data)
