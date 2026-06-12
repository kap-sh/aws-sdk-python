"""Generated from Smithy shape ``com.amazonaws.transfer#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "SFTP",
    "FTP",
    "FTPS",
    "AS2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SFTP",
        "FTP",
        "FTPS",
        "AS2",
    )
)


def serialize_aws_json_1_1(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
