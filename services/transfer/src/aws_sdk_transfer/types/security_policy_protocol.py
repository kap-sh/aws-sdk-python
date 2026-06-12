"""Generated from Smithy shape ``com.amazonaws.transfer#SecurityPolicyProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

SecurityPolicyProtocol: TypeAlias = Literal[
    "SFTP",
    "FTPS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SFTP",
        "FTPS",
    )
)


def serialize_aws_json_1_1(value: SecurityPolicyProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityPolicyProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecurityPolicyProtocol value: {data!r}")
    return cast(SecurityPolicyProtocol, data)
