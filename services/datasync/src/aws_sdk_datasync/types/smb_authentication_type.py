"""Generated from Smithy shape ``com.amazonaws.datasync#SmbAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

SmbAuthenticationType: TypeAlias = Literal[
    "NTLM",
    "KERBEROS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NTLM",
        "KERBEROS",
    )
)


def serialize_aws_json_1_1(value: SmbAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SmbAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SmbAuthenticationType value: {data!r}")
    return cast(SmbAuthenticationType, data)
