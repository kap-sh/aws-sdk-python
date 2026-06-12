"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

ConnectionTypeStatus: TypeAlias = Literal[
    "ACTIVE",
    "CANCELED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CANCELED",
    )
)


def serialize_aws_json_1_0(value: ConnectionTypeStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionTypeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionTypeStatus value: {data!r}")
    return cast(ConnectionTypeStatus, data)
