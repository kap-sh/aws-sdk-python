"""Generated from Smithy shape ``com.amazonaws.workmail#CancelMailboxExportJobResponse``."""

from typing import TypedDict


class CancelMailboxExportJobResponse(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMailboxExportJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMailboxExportJobResponse:
    out: CancelMailboxExportJobResponse = {}  # type: ignore[typeddict-item]
    return out
