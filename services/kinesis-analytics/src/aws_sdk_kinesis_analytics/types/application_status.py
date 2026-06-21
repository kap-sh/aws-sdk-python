"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationStatus: TypeAlias = Literal[
    "DELETING",
    "STARTING",
    "STOPPING",
    "READY",
    "RUNNING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationStatus:
    return cast(ApplicationStatus, data)
