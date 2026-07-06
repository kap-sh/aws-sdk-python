"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeSecurityHubV2Request``."""

from typing_extensions import TypedDict


class DescribeSecurityHubV2Request(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityHubV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSecurityHubV2Request:
    out: DescribeSecurityHubV2Request = {}  # type: ignore[typeddict-item]
    return out
