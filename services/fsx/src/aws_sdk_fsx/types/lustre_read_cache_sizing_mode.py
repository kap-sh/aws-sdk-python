"""Generated from Smithy shape ``com.amazonaws.fsx#LustreReadCacheSizingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

LustreReadCacheSizingMode: TypeAlias = Literal[
    "NO_CACHE",
    "USER_PROVISIONED",
    "PROPORTIONAL_TO_THROUGHPUT_CAPACITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_CACHE",
        "USER_PROVISIONED",
        "PROPORTIONAL_TO_THROUGHPUT_CAPACITY",
    )
)


def serialize_aws_json_1_1(value: LustreReadCacheSizingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LustreReadCacheSizingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LustreReadCacheSizingMode value: {data!r}")
    return cast(LustreReadCacheSizingMode, data)
