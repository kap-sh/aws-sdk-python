"""Generated from Smithy shape ``com.amazonaws.datasync#SmbSecurityDescriptorCopyFlags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

SmbSecurityDescriptorCopyFlags: TypeAlias = Literal[
    "NONE",
    "OWNER_DACL",
    "OWNER_DACL_SACL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "OWNER_DACL",
        "OWNER_DACL_SACL",
    )
)


def serialize_aws_json_1_1(value: SmbSecurityDescriptorCopyFlags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SmbSecurityDescriptorCopyFlags:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmbSecurityDescriptorCopyFlags value: {data!r}"
        )
    return cast(SmbSecurityDescriptorCopyFlags, data)
