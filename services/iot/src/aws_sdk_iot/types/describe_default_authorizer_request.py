"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDefaultAuthorizerRequest``."""

from typing_extensions import TypedDict


class DescribeDefaultAuthorizerRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDefaultAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDefaultAuthorizerRequest:
    out: DescribeDefaultAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
