"""Generated from Smithy shape ``com.amazonaws.deadline#LicenseEndpointSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.license_endpoint_summary

LicenseEndpointSummaries: TypeAlias = list[
    "capo_deadline.types.license_endpoint_summary.LicenseEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseEndpointSummaries) -> list:
    import capo_deadline.types.license_endpoint_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.license_endpoint_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LicenseEndpointSummaries:
    import capo_deadline.types.license_endpoint_summary

    out: LicenseEndpointSummaries = []
    for item in data:
        out.append(capo_deadline.types.license_endpoint_summary.deserialize_json(item))
    return out
