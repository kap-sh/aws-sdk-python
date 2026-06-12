"""Generated from Smithy shape ``com.amazonaws.fsx#NfsVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

NfsVersion: TypeAlias = Literal["NFS3",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NFS3",))


def serialize_aws_json_1_1(value: NfsVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NfsVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NfsVersion value: {data!r}")
    return cast(NfsVersion, data)
