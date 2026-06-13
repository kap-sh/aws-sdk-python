"""Generated from Smithy shape ``com.amazonaws.odb#RefreshableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

RefreshableStatus: TypeAlias = Literal[
    "REFRESHING",
    "NOT_REFRESHING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REFRESHING",
        "NOT_REFRESHING",
    )
)


def serialize_aws_json_1_0(value: RefreshableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RefreshableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RefreshableStatus value: {data!r}")
    return cast(RefreshableStatus, data)
