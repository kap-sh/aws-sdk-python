"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ImportStatus``."""

from typing import Literal, TypeAlias, cast

ImportStatus: TypeAlias = Literal[
    "IMPORT_IN_PROGRESS",
    "IMPORT_COMPLETE",
    "IMPORT_COMPLETE_WITH_ERRORS",
    "IMPORT_FAILED",
    "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
    "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
    "IMPORT_FAILED_UNSUPPORTED_FILE_TYPE",
    "DELETE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_FAILED_LIMIT_EXCEEDED",
    "INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportStatus:
    return cast(ImportStatus, data)
