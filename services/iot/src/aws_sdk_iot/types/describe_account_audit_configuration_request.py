"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAccountAuditConfigurationRequest``."""

from typing import TypedDict


class DescribeAccountAuditConfigurationRequest(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountAuditConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccountAuditConfigurationRequest:
    out: DescribeAccountAuditConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
