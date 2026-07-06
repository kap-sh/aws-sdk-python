"""Generated from Smithy shape ``com.amazonaws.iot#DescribeEventConfigurationsRequest``."""

from typing_extensions import TypedDict


class DescribeEventConfigurationsRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEventConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEventConfigurationsRequest:
    out: DescribeEventConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
