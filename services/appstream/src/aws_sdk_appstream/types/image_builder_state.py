"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ImageBuilderState: TypeAlias = Literal[
    "PENDING",
    "UPDATING_AGENT",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "REBOOTING",
    "SNAPSHOTTING",
    "DELETING",
    "FAILED",
    "UPDATING",
    "PENDING_QUALIFICATION",
    "PENDING_SYNCING_APPS",
    "SYNCING_APPS",
    "PENDING_IMAGE_IMPORT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "UPDATING_AGENT",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "REBOOTING",
        "SNAPSHOTTING",
        "DELETING",
        "FAILED",
        "UPDATING",
        "PENDING_QUALIFICATION",
        "PENDING_SYNCING_APPS",
        "SYNCING_APPS",
        "PENDING_IMAGE_IMPORT",
    )
)


def serialize_aws_json_1_1(value: ImageBuilderState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageBuilderState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageBuilderState value: {data!r}")
    return cast(ImageBuilderState, data)
