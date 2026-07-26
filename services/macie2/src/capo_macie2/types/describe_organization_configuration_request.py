"""Generated from Smithy shape ``com.amazonaws.macie2#DescribeOrganizationConfigurationRequest``."""

from typing_extensions import TypedDict


class DescribeOrganizationConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeOrganizationConfigurationRequest:
    out: DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
