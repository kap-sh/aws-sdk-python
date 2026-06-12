"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsDataTransferProtection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

HdfsDataTransferProtection: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: HdfsDataTransferProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HdfsDataTransferProtection:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HdfsDataTransferProtection value: {data!r}"
        )
    return cast(HdfsDataTransferProtection, data)
