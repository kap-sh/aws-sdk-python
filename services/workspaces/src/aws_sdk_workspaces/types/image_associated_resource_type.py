"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ImageAssociatedResourceType: TypeAlias = Literal["APPLICATION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("APPLICATION",))


def serialize_aws_json_1_1(value: ImageAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageAssociatedResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ImageAssociatedResourceType value: {data!r}"
        )
    return cast(ImageAssociatedResourceType, data)
