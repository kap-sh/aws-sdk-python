"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeOrganizationConfigurationRequest``."""

from typing import TypedDict


class DescribeOrganizationConfigurationRequest(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeOrganizationConfigurationRequest:
    out: DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
