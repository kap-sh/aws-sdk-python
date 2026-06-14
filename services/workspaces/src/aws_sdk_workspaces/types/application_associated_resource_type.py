"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ApplicationAssociatedResourceType: TypeAlias = Literal[
    "WORKSPACE",
    "BUNDLE",
    "IMAGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WORKSPACE",
        "BUNDLE",
        "IMAGE",
    )
)


def serialize_aws_json_1_1(value: ApplicationAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationAssociatedResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ApplicationAssociatedResourceType value: {data!r}"
        )
    return cast(ApplicationAssociatedResourceType, data)
