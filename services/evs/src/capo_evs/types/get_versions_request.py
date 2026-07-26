"""Generated from Smithy shape ``com.amazonaws.evs#GetVersionsRequest``."""

from typing_extensions import TypedDict


class GetVersionsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVersionsRequest:
    out: GetVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
