"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateMailboxQuotaResponse``."""

from typing_extensions import TypedDict


class UpdateMailboxQuotaResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMailboxQuotaResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMailboxQuotaResponse:
    out: UpdateMailboxQuotaResponse = {}  # type: ignore[typeddict-item]
    return out
