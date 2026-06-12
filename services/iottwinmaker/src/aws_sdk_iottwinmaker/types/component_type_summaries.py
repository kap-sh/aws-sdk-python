"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentTypeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_summary

ComponentTypeSummaries: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.component_type_summary.ComponentTypeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentTypeSummaries) -> list:
    import aws_sdk_iottwinmaker.types.component_type_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.component_type_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComponentTypeSummaries:
    import aws_sdk_iottwinmaker.types.component_type_summary

    out: ComponentTypeSummaries = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.component_type_summary.deserialize_json(item)
        )
    return out
