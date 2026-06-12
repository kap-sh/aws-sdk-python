"""Generated from Smithy shape ``com.amazonaws.iot#DescribeEventConfigurationsRequest``."""

from typing import TypedDict


class DescribeEventConfigurationsRequest(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEventConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEventConfigurationsRequest:
    out: DescribeEventConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
