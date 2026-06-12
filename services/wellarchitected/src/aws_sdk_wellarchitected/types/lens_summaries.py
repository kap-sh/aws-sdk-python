"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_summary

LensSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.lens_summary.LensSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LensSummaries) -> list:
    import aws_sdk_wellarchitected.types.lens_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.lens_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LensSummaries:
    import aws_sdk_wellarchitected.types.lens_summary

    out: LensSummaries = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.lens_summary.deserialize_json(item))
    return out
