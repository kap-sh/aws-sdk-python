"""Generated from Smithy shape ``com.amazonaws.odb#RefreshableMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

RefreshableMode: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "MANUAL",
    )
)


def serialize_aws_json_1_0(value: RefreshableMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RefreshableMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RefreshableMode value: {data!r}")
    return cast(RefreshableMode, data)
