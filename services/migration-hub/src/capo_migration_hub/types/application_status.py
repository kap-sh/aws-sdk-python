"""Generated from Smithy shape ``com.amazonaws.migrationhub#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationStatus:
    return cast(ApplicationStatus, data)
