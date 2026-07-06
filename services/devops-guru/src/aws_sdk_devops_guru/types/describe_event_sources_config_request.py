"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeEventSourcesConfigRequest``."""

from typing_extensions import TypedDict


class DescribeEventSourcesConfigRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEventSourcesConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEventSourcesConfigRequest:
    out: DescribeEventSourcesConfigRequest = {}  # type: ignore[typeddict-item]
    return out
