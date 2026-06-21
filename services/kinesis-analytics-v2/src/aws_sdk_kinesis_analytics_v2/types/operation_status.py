"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#OperationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the operation.</p>"""
OperationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELLED",
    "SUCCESSFUL",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationStatus:
    return cast(OperationStatus, data)
