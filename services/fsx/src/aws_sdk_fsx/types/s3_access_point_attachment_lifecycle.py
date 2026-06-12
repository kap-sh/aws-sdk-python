"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

S3AccessPointAttachmentLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "UPDATING",
    "FAILED",
    "MISCONFIGURED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "CREATING",
        "DELETING",
        "UPDATING",
        "FAILED",
        "MISCONFIGURED",
    )
)


def serialize_aws_json_1_1(value: S3AccessPointAttachmentLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AccessPointAttachmentLifecycle:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown S3AccessPointAttachmentLifecycle value: {data!r}"
        )
    return cast(S3AccessPointAttachmentLifecycle, data)
