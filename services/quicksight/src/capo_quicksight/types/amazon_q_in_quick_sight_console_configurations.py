"""Generated from Smithy shape ``com.amazonaws.quicksight#AmazonQInQuickSightConsoleConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_qn_a_configurations
    import capo_quicksight.types.data_stories_configurations
    import capo_quicksight.types.executive_summary_configurations
    import capo_quicksight.types.generative_authoring_configurations


class AmazonQInQuickSightConsoleConfigurations(TypedDict, closed=True):
    data_qn_a: NotRequired[
        "capo_quicksight.types.data_qn_a_configurations.DataQnAConfigurations"
    ]
    """<p>Adds generative Q&A capabilitiees to an embedded Quick Sight console.</p>"""
    generative_authoring: NotRequired[
        "capo_quicksight.types.generative_authoring_configurations.GenerativeAuthoringConfigurations"
    ]
    """<p>Adds the generative BI authoring experience to an embedded Quick Sight console.</p>"""
    executive_summary: NotRequired[
        "capo_quicksight.types.executive_summary_configurations.ExecutiveSummaryConfigurations"
    ]
    """<p>Adds the executive summaries feature to an embedded Quick Sight console.</p>"""
    data_stories: NotRequired[
        "capo_quicksight.types.data_stories_configurations.DataStoriesConfigurations"
    ]
    """<p>Adds the data stories feature to an embedded Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonQInQuickSightConsoleConfigurations) -> dict:
    out: dict = {}
    if "data_qn_a" in value:
        import capo_quicksight.types.data_qn_a_configurations

        out["DataQnA"] = capo_quicksight.types.data_qn_a_configurations.serialize_json(
            value["data_qn_a"]
        )
    if "generative_authoring" in value:
        import capo_quicksight.types.generative_authoring_configurations

        out["GenerativeAuthoring"] = (
            capo_quicksight.types.generative_authoring_configurations.serialize_json(
                value["generative_authoring"]
            )
        )
    if "executive_summary" in value:
        import capo_quicksight.types.executive_summary_configurations

        out["ExecutiveSummary"] = (
            capo_quicksight.types.executive_summary_configurations.serialize_json(
                value["executive_summary"]
            )
        )
    if "data_stories" in value:
        import capo_quicksight.types.data_stories_configurations

        out["DataStories"] = (
            capo_quicksight.types.data_stories_configurations.serialize_json(
                value["data_stories"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonQInQuickSightConsoleConfigurations:
    out: AmazonQInQuickSightConsoleConfigurations = {}  # type: ignore[typeddict-item]
    if "DataQnA" in data:
        import capo_quicksight.types.data_qn_a_configurations

        out["data_qn_a"] = (
            capo_quicksight.types.data_qn_a_configurations.deserialize_json(
                data["DataQnA"]
            )
        )
    if "GenerativeAuthoring" in data:
        import capo_quicksight.types.generative_authoring_configurations

        out["generative_authoring"] = (
            capo_quicksight.types.generative_authoring_configurations.deserialize_json(
                data["GenerativeAuthoring"]
            )
        )
    if "ExecutiveSummary" in data:
        import capo_quicksight.types.executive_summary_configurations

        out["executive_summary"] = (
            capo_quicksight.types.executive_summary_configurations.deserialize_json(
                data["ExecutiveSummary"]
            )
        )
    if "DataStories" in data:
        import capo_quicksight.types.data_stories_configurations

        out["data_stories"] = (
            capo_quicksight.types.data_stories_configurations.deserialize_json(
                data["DataStories"]
            )
        )
    return out
