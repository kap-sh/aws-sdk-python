"""Generated from Smithy shape ``com.amazonaws.wafv2#IPAddressVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

IPAddressVersion: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
    )
)


def serialize_aws_json_1_1(value: IPAddressVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IPAddressVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IPAddressVersion value: {data!r}")
    return cast(IPAddressVersion, data)
