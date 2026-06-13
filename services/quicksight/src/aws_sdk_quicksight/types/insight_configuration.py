"""Generated from Smithy shape ``com.amazonaws.quicksight#InsightConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.computation_list
    import aws_sdk_quicksight.types.custom_narrative_options
    import aws_sdk_quicksight.types.visual_interaction_options


class InsightConfiguration(TypedDict):
    computations: NotRequired[
        "aws_sdk_quicksight.types.computation_list.ComputationList"
    ]
    """<p>The computations configurations of the insight visual</p>"""
    custom_narrative: NotRequired[
        "aws_sdk_quicksight.types.custom_narrative_options.CustomNarrativeOptions"
    ]
    """<p>The custom narrative of the insight visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightConfiguration) -> dict:
    out: dict = {}
    if "computations" in value:
        import aws_sdk_quicksight.types.computation_list

        out["Computations"] = aws_sdk_quicksight.types.computation_list.serialize_json(
            value["computations"]
        )
    if "custom_narrative" in value:
        import aws_sdk_quicksight.types.custom_narrative_options

        out["CustomNarrative"] = (
            aws_sdk_quicksight.types.custom_narrative_options.serialize_json(
                value["custom_narrative"]
            )
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> InsightConfiguration:
    out: InsightConfiguration = {}  # type: ignore[typeddict-item]
    if "Computations" in data:
        import aws_sdk_quicksight.types.computation_list

        out["computations"] = (
            aws_sdk_quicksight.types.computation_list.deserialize_json(
                data["Computations"]
            )
        )
    if "CustomNarrative" in data:
        import aws_sdk_quicksight.types.custom_narrative_options

        out["custom_narrative"] = (
            aws_sdk_quicksight.types.custom_narrative_options.deserialize_json(
                data["CustomNarrative"]
            )
        )
    if "Interactions" in data:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
