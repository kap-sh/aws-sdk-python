"""Generated from Smithy shape ``com.amazonaws.fsx#BackupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

"""<p>The type of the backup.</p>"""
BackupType: TypeAlias = Literal[
    "AUTOMATIC",
    "USER_INITIATED",
    "AWS_BACKUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "USER_INITIATED",
        "AWS_BACKUP",
    )
)


def serialize_aws_json_1_1(value: BackupType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupType value: {data!r}")
    return cast(BackupType, data)
