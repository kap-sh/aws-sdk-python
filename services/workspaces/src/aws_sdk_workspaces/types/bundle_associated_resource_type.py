"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

BundleAssociatedResourceType: TypeAlias = Literal["APPLICATION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("APPLICATION",))


def serialize_aws_json_1_1(value: BundleAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BundleAssociatedResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BundleAssociatedResourceType value: {data!r}"
        )
    return cast(BundleAssociatedResourceType, data)
