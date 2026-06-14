"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspaceRelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

StandbyWorkspaceRelationshipType: TypeAlias = Literal[
    "PRIMARY",
    "STANDBY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "STANDBY",
    )
)


def serialize_aws_json_1_1(value: StandbyWorkspaceRelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StandbyWorkspaceRelationshipType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StandbyWorkspaceRelationshipType value: {data!r}"
        )
    return cast(StandbyWorkspaceRelationshipType, data)
