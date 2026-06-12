"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ManagedResourceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.managed_resource_summary

ManagedResourceSummaries: TypeAlias = list[
    "aws_sdk_arc_zonal_shift.types.managed_resource_summary.ManagedResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedResourceSummaries) -> list:
    import aws_sdk_arc_zonal_shift.types.managed_resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_zonal_shift.types.managed_resource_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ManagedResourceSummaries:
    import aws_sdk_arc_zonal_shift.types.managed_resource_summary

    out: ManagedResourceSummaries = []
    for item in data:
        out.append(
            aws_sdk_arc_zonal_shift.types.managed_resource_summary.deserialize_json(
                item
            )
        )
    return out
