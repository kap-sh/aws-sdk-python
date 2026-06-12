"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_summary

ComponentSummaries: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.component_summary.ComponentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentSummaries) -> list:
    import aws_sdk_iottwinmaker.types.component_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.component_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentSummaries:
    import aws_sdk_iottwinmaker.types.component_summary

    out: ComponentSummaries = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.component_summary.deserialize_json(item))
    return out
