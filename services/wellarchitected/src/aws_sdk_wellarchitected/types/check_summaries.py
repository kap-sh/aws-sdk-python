"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.check_summary

CheckSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.check_summary.CheckSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckSummaries) -> list:
    import aws_sdk_wellarchitected.types.check_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.check_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckSummaries:
    import aws_sdk_wellarchitected.types.check_summary

    out: CheckSummaries = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.check_summary.deserialize_json(item))
    return out
