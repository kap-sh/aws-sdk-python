"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeleteChannelResponse``."""

from typing_extensions import TypedDict


class DeleteChannelResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteChannelResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteChannelResponse:
    out: DeleteChannelResponse = {}  # type: ignore[typeddict-item]
    return out
