"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileShareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

"""<p>The type of the file share.</p>"""
FileShareType: TypeAlias = Literal[
    "NFS",
    "SMB",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NFS",
        "SMB",
    )
)


def serialize_aws_json_1_1(value: FileShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileShareType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileShareType value: {data!r}")
    return cast(FileShareType, data)
