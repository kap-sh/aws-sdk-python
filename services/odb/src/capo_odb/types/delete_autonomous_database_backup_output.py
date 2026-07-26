"""Generated from Smithy shape ``com.amazonaws.odb#DeleteAutonomousDatabaseBackupOutput``."""

from typing_extensions import TypedDict


class DeleteAutonomousDatabaseBackupOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAutonomousDatabaseBackupOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAutonomousDatabaseBackupOutput:
    out: DeleteAutonomousDatabaseBackupOutput = {}  # type: ignore[typeddict-item]
    return out
