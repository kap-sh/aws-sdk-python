"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageRequiredTenancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkspaceImageRequiredTenancy: TypeAlias = Literal[
    "DEFAULT",
    "DEDICATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "DEDICATED",
    )
)


def serialize_aws_json_1_1(value: WorkspaceImageRequiredTenancy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceImageRequiredTenancy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkspaceImageRequiredTenancy value: {data!r}"
        )
    return cast(WorkspaceImageRequiredTenancy, data)
