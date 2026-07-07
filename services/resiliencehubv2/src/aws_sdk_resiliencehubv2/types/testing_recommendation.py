"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestingRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.suggested_changes_list


class TestingRecommendation(TypedDict, closed=True):
    suggested_changes: NotRequired[
        "aws_sdk_resiliencehubv2.types.suggested_changes_list.SuggestedChangesList"
    ]
    """<p>The list of suggested testing changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestingRecommendation) -> dict:
    out: dict = {}
    if "suggested_changes" in value:
        import aws_sdk_resiliencehubv2.types.suggested_changes_list

        out["suggestedChanges"] = (
            aws_sdk_resiliencehubv2.types.suggested_changes_list.serialize_json(
                value["suggested_changes"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestingRecommendation:
    out: TestingRecommendation = {}  # type: ignore[typeddict-item]
    if "suggestedChanges" in data:
        import aws_sdk_resiliencehubv2.types.suggested_changes_list

        out["suggested_changes"] = (
            aws_sdk_resiliencehubv2.types.suggested_changes_list.deserialize_json(
                data["suggestedChanges"]
            )
        )
    return out
