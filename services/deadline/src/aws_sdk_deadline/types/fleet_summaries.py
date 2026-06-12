"""Generated from Smithy shape ``com.amazonaws.deadline#FleetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_summary

FleetSummaries: TypeAlias = list["aws_sdk_deadline.types.fleet_summary.FleetSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: FleetSummaries) -> list:
    import aws_sdk_deadline.types.fleet_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.fleet_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetSummaries:
    import aws_sdk_deadline.types.fleet_summary

    out: FleetSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.fleet_summary.deserialize_json(item))
    return out
