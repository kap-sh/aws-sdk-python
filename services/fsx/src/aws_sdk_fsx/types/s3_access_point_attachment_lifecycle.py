"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentLifecycle``."""

from typing import Literal, TypeAlias, cast

S3AccessPointAttachmentLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "UPDATING",
    "FAILED",
    "MISCONFIGURED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachmentLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AccessPointAttachmentLifecycle:
    return cast(S3AccessPointAttachmentLifecycle, data)
