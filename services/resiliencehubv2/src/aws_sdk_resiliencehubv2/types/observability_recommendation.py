"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ObservabilityRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.suggested_changes_list


class ObservabilityRecommendation(TypedDict):
    suggested_changes: NotRequired[
        "aws_sdk_resiliencehubv2.types.suggested_changes_list.SuggestedChangesList"
    ]
    """<p>The list of suggested observability changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObservabilityRecommendation) -> dict:
    out: dict = {}
    if "suggested_changes" in value:
        import aws_sdk_resiliencehubv2.types.suggested_changes_list

        out["suggestedChanges"] = (
            aws_sdk_resiliencehubv2.types.suggested_changes_list.serialize_json(
                value["suggested_changes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObservabilityRecommendation:
    out: ObservabilityRecommendation = {}  # type: ignore[typeddict-item]
    if "suggestedChanges" in data:
        import aws_sdk_resiliencehubv2.types.suggested_changes_list

        out["suggested_changes"] = (
            aws_sdk_resiliencehubv2.types.suggested_changes_list.deserialize_json(
                data["suggestedChanges"]
            )
        )
    return out
