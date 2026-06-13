"""Generated from Smithy shape ``com.amazonaws.mailmanager#IpType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IpType: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: IpType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IpType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpType value: {data!r}")
    return cast(IpType, data)
