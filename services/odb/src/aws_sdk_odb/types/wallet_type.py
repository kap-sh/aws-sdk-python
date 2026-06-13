"""Generated from Smithy shape ``com.amazonaws.odb#WalletType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

WalletType: TypeAlias = Literal[
    "REGIONAL",
    "INSTANCE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGIONAL",
        "INSTANCE",
    )
)


def serialize_aws_json_1_0(value: WalletType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WalletType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WalletType value: {data!r}")
    return cast(WalletType, data)
