"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

S3AccessPointAttachmentType: TypeAlias = Literal[
    "OPENZFS",
    "ONTAP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPENZFS",
        "ONTAP",
    )
)


def serialize_aws_json_1_1(value: S3AccessPointAttachmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AccessPointAttachmentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown S3AccessPointAttachmentType value: {data!r}"
        )
    return cast(S3AccessPointAttachmentType, data)
