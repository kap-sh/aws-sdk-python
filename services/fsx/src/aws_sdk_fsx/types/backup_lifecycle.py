"""Generated from Smithy shape ``com.amazonaws.fsx#BackupLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

"""<p>The lifecycle status of the backup.</p> <ul> <li> <p> <code>AVAILABLE</code> - The backup is fully available.</p> </li> <li> <p> <code>PENDING</code> - For user-initiated backups on Lustre file systems only; Amazon FSx hasn't started creating the backup.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the new user-initiated backup.</p> </li> <li> <p> <code>TRANSFERRING</code> - For user-initiated backups on Lustre file systems only; Amazon FSx is backing up the file system.</p> </li> <li> <p> <code>COPYING</code> - Amazon FSx is copying the backup.</p> </li> <li> <p> <code>DELETED</code> - Amazon FSx deleted the backup and it's no longer available.</p> </li> <li> <p> <code>FAILED</code> - Amazon FSx couldn't finish the backup.</p> </li> </ul>"""
BackupLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "TRANSFERRING",
    "DELETED",
    "FAILED",
    "PENDING",
    "COPYING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "CREATING",
        "TRANSFERRING",
        "DELETED",
        "FAILED",
        "PENDING",
        "COPYING",
    )
)


def serialize_aws_json_1_1(value: BackupLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupLifecycle value: {data!r}")
    return cast(BackupLifecycle, data)
