"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SceneSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.scene_summary

SceneSummaries: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.scene_summary.SceneSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SceneSummaries) -> list:
    import aws_sdk_iottwinmaker.types.scene_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.scene_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SceneSummaries:
    import aws_sdk_iottwinmaker.types.scene_summary

    out: SceneSummaries = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.scene_summary.deserialize_json(item))
    return out
