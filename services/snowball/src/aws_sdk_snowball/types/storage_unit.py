"""Generated from Smithy shape ``com.amazonaws.snowball#StorageUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

StorageUnit: TypeAlias = Literal["TB",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TB",))


def serialize_aws_json_1_1(value: StorageUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageUnit value: {data!r}")
    return cast(StorageUnit, data)
