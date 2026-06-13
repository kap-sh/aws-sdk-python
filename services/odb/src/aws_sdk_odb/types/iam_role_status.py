"""Generated from Smithy shape ``com.amazonaws.odb#IamRoleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

IamRoleStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "DISASSOCIATING",
    "FAILED",
    "CONNECTED",
    "DISCONNECTED",
    "PARTIALLY_CONNECTED",
    "UNKNOWN",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATING",
        "DISASSOCIATING",
        "FAILED",
        "CONNECTED",
        "DISCONNECTED",
        "PARTIALLY_CONNECTED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_0(value: IamRoleStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IamRoleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IamRoleStatus value: {data!r}")
    return cast(IamRoleStatus, data)
