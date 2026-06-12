"""Generated from Smithy shape ``com.amazonaws.datasync#EfsInTransitEncryption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

EfsInTransitEncryption: TypeAlias = Literal[
    "NONE",
    "TLS1_2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "TLS1_2",
    )
)


def serialize_aws_json_1_1(value: EfsInTransitEncryption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EfsInTransitEncryption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EfsInTransitEncryption value: {data!r}")
    return cast(EfsInTransitEncryption, data)
