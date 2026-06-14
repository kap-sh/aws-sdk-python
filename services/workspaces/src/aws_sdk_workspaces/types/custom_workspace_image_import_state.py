"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomWorkspaceImageImportState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

CustomWorkspaceImageImportState: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "PROCESSING_SOURCE_IMAGE",
    "IMAGE_TESTING_START",
    "UPDATING_OPERATING_SYSTEM",
    "IMAGE_COMPATIBILITY_CHECKING",
    "IMAGE_TESTING_GENERALIZATION",
    "CREATING_TEST_INSTANCE",
    "INSTALLING_COMPONENTS",
    "GENERALIZING",
    "VALIDATING",
    "PUBLISHING",
    "COMPLETED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "PROCESSING_SOURCE_IMAGE",
        "IMAGE_TESTING_START",
        "UPDATING_OPERATING_SYSTEM",
        "IMAGE_COMPATIBILITY_CHECKING",
        "IMAGE_TESTING_GENERALIZATION",
        "CREATING_TEST_INSTANCE",
        "INSTALLING_COMPONENTS",
        "GENERALIZING",
        "VALIDATING",
        "PUBLISHING",
        "COMPLETED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: CustomWorkspaceImageImportState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomWorkspaceImageImportState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomWorkspaceImageImportState value: {data!r}"
        )
    return cast(CustomWorkspaceImageImportState, data)
