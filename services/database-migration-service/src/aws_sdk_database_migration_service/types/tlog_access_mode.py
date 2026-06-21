"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TlogAccessMode``."""

from typing import Literal, TypeAlias, cast

TlogAccessMode: TypeAlias = Literal[
    "BackupOnly",
    "PreferBackup",
    "PreferTlog",
    "TlogOnly",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TlogAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TlogAccessMode:
    return cast(TlogAccessMode, data)
