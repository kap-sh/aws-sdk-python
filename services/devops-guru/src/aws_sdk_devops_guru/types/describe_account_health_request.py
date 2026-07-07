"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeAccountHealthRequest``."""

from typing_extensions import TypedDict


class DescribeAccountHealthRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountHealthRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccountHealthRequest:
    out: DescribeAccountHealthRequest = {}  # type: ignore[typeddict-item]
    return out
