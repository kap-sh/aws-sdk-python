"""Generated from Smithy shape ``com.amazonaws.deadline#VolumeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.volume_summary

VolumeSummaries: TypeAlias = list["aws_sdk_deadline.types.volume_summary.VolumeSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeSummaries) -> list:
    import aws_sdk_deadline.types.volume_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.volume_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> VolumeSummaries:
    import aws_sdk_deadline.types.volume_summary

    out: VolumeSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.volume_summary.deserialize_json(item))
    return out
