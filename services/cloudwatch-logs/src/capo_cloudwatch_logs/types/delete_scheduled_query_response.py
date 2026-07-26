"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteScheduledQueryResponse``."""

from typing_extensions import TypedDict


class DeleteScheduledQueryResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteScheduledQueryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteScheduledQueryResponse:
    out: DeleteScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    return out
