"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#AliasState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

AliasState: TypeAlias = Literal[
    "Active",
    "PendingDeletion",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "PendingDeletion",
    )
)


def serialize_aws_json_1_0(value: AliasState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AliasState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AliasState value: {data!r}")
    return cast(AliasState, data)
