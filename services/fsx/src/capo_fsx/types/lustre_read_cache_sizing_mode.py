"""Generated from Smithy shape ``com.amazonaws.fsx#LustreReadCacheSizingMode``."""

from typing import Literal, TypeAlias, cast

LustreReadCacheSizingMode: TypeAlias = Literal[
    "NO_CACHE",
    "USER_PROVISIONED",
    "PROPORTIONAL_TO_THROUGHPUT_CAPACITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreReadCacheSizingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LustreReadCacheSizingMode:
    return cast(LustreReadCacheSizingMode, data)
