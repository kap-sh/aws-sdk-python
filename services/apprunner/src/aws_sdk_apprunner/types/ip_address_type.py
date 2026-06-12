"""Generated from Smithy shape ``com.amazonaws.apprunner#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUAL_STACK",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUAL_STACK",
    )
)


def serialize_aws_json_1_0(value: IpAddressType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {data!r}")
    return cast(IpAddressType, data)
