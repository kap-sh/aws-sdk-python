"""Generated from Smithy shape ``com.amazonaws.quicksight#AmazonQInQuickSightConsoleConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_qn_a_configurations
    import aws_sdk_quicksight.types.data_stories_configurations
    import aws_sdk_quicksight.types.executive_summary_configurations
    import aws_sdk_quicksight.types.generative_authoring_configurations


class AmazonQInQuickSightConsoleConfigurations(TypedDict):
    data_qn_a: NotRequired[
        "aws_sdk_quicksight.types.data_qn_a_configurations.DataQnAConfigurations"
    ]
    """<p>Adds generative Q&A capabilitiees to an embedded Quick Sight console.</p>"""
    generative_authoring: NotRequired[
        "aws_sdk_quicksight.types.generative_authoring_configurations.GenerativeAuthoringConfigurations"
    ]
    """<p>Adds the generative BI authoring experience to an embedded Quick Sight console.</p>"""
    executive_summary: NotRequired[
        "aws_sdk_quicksight.types.executive_summary_configurations.ExecutiveSummaryConfigurations"
    ]
    """<p>Adds the executive summaries feature to an embedded Quick Sight console.</p>"""
    data_stories: NotRequired[
        "aws_sdk_quicksight.types.data_stories_configurations.DataStoriesConfigurations"
    ]
    """<p>Adds the data stories feature to an embedded Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonQInQuickSightConsoleConfigurations) -> dict:
    out: dict = {}
    if "data_qn_a" in value:
        import aws_sdk_quicksight.types.data_qn_a_configurations

        out["DataQnA"] = (
            aws_sdk_quicksight.types.data_qn_a_configurations.serialize_json(
                value["data_qn_a"]
            )
        )
    if "generative_authoring" in value:
        import aws_sdk_quicksight.types.generative_authoring_configurations

        out["GenerativeAuthoring"] = (
            aws_sdk_quicksight.types.generative_authoring_configurations.serialize_json(
                value["generative_authoring"]
            )
        )
    if "executive_summary" in value:
        import aws_sdk_quicksight.types.executive_summary_configurations

        out["ExecutiveSummary"] = (
            aws_sdk_quicksight.types.executive_summary_configurations.serialize_json(
                value["executive_summary"]
            )
        )
    if "data_stories" in value:
        import aws_sdk_quicksight.types.data_stories_configurations

        out["DataStories"] = (
            aws_sdk_quicksight.types.data_stories_configurations.serialize_json(
                value["data_stories"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonQInQuickSightConsoleConfigurations:
    out: AmazonQInQuickSightConsoleConfigurations = {}  # type: ignore[typeddict-item]
    if "DataQnA" in data:
        import aws_sdk_quicksight.types.data_qn_a_configurations

        out["data_qn_a"] = (
            aws_sdk_quicksight.types.data_qn_a_configurations.deserialize_json(
                data["DataQnA"]
            )
        )
    if "GenerativeAuthoring" in data:
        import aws_sdk_quicksight.types.generative_authoring_configurations

        out["generative_authoring"] = (
            aws_sdk_quicksight.types.generative_authoring_configurations.deserialize_json(
                data["GenerativeAuthoring"]
            )
        )
    if "ExecutiveSummary" in data:
        import aws_sdk_quicksight.types.executive_summary_configurations

        out["executive_summary"] = (
            aws_sdk_quicksight.types.executive_summary_configurations.deserialize_json(
                data["ExecutiveSummary"]
            )
        )
    if "DataStories" in data:
        import aws_sdk_quicksight.types.data_stories_configurations

        out["data_stories"] = (
            aws_sdk_quicksight.types.data_stories_configurations.deserialize_json(
                data["DataStories"]
            )
        )
    return out
