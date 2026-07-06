"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeleteArchiveResponse``."""

from typing_extensions import TypedDict


class DeleteArchiveResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteArchiveResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteArchiveResponse:
    out: DeleteArchiveResponse = {}  # type: ignore[typeddict-item]
    return out
