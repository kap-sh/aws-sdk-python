"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

FileCacheType: TypeAlias = Literal["LUSTRE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LUSTRE",))


def serialize_aws_json_1_1(value: FileCacheType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileCacheType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileCacheType value: {data!r}")
    return cast(FileCacheType, data)
