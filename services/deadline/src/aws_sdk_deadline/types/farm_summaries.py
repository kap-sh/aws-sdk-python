"""Generated from Smithy shape ``com.amazonaws.deadline#FarmSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_summary

FarmSummaries: TypeAlias = list["aws_sdk_deadline.types.farm_summary.FarmSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: FarmSummaries) -> list:
    import aws_sdk_deadline.types.farm_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.farm_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FarmSummaries:
    import aws_sdk_deadline.types.farm_summary

    out: FarmSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.farm_summary.deserialize_json(item))
    return out
