"""Generated from Smithy shape ``com.amazonaws.transfer#TransferTableStatus``."""

from typing import Literal, TypeAlias, cast

TransferTableStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferTableStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransferTableStatus:
    return cast(TransferTableStatus, data)
