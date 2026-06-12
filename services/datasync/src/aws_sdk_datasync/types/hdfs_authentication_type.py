"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

HdfsAuthenticationType: TypeAlias = Literal[
    "SIMPLE",
    "KERBEROS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIMPLE",
        "KERBEROS",
    )
)


def serialize_aws_json_1_1(value: HdfsAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HdfsAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HdfsAuthenticationType value: {data!r}")
    return cast(HdfsAuthenticationType, data)
