"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsRpcProtection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

HdfsRpcProtection: TypeAlias = Literal[
    "DISABLED",
    "AUTHENTICATION",
    "INTEGRITY",
    "PRIVACY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "AUTHENTICATION",
        "INTEGRITY",
        "PRIVACY",
    )
)


def serialize_aws_json_1_1(value: HdfsRpcProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HdfsRpcProtection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HdfsRpcProtection value: {data!r}")
    return cast(HdfsRpcProtection, data)
