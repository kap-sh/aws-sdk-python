"""Generated from Smithy shape ``com.amazonaws.deadline#FleetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.fleet_summary

FleetSummaries: TypeAlias = list["capo_deadline.types.fleet_summary.FleetSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: FleetSummaries) -> list:
    import capo_deadline.types.fleet_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.fleet_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FleetSummaries:
    import capo_deadline.types.fleet_summary

    out: FleetSummaries = []
    for item in data:
        out.append(capo_deadline.types.fleet_summary.deserialize_json(item))
    return out
