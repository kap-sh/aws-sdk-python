"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentsFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

S3AccessPointAttachmentsFilterName: TypeAlias = Literal[
    "file-system-id",
    "volume-id",
    "type",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "file-system-id",
        "volume-id",
        "type",
    )
)


def serialize_aws_json_1_1(value: S3AccessPointAttachmentsFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AccessPointAttachmentsFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown S3AccessPointAttachmentsFilterName value: {data!r}"
        )
    return cast(S3AccessPointAttachmentsFilterName, data)
