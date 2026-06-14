"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkSpaceAssociatedResourceType: TypeAlias = Literal["APPLICATION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("APPLICATION",))


def serialize_aws_json_1_1(value: WorkSpaceAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkSpaceAssociatedResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkSpaceAssociatedResourceType value: {data!r}"
        )
    return cast(WorkSpaceAssociatedResourceType, data)
