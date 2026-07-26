"""Generated from Smithy shape ``com.amazonaws.fsx#BackupType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of the backup.</p>"""
BackupType: TypeAlias = Literal[
    "AUTOMATIC",
    "USER_INITIATED",
    "AWS_BACKUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupType:
    return cast(BackupType, data)
