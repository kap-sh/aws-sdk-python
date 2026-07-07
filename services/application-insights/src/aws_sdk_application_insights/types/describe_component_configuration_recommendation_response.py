"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeComponentConfigurationRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.component_configuration


class DescribeComponentConfigurationRecommendationResponse(TypedDict, closed=True):
    component_configuration: NotRequired[
        "aws_sdk_application_insights.types.component_configuration.ComponentConfiguration"
    ]
    """<p>The recommended configuration settings of the component. The value is the escaped JSON of the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeComponentConfigurationRecommendationResponse,
) -> dict:
    out: dict = {}
    if "component_configuration" in value:
        out["ComponentConfiguration"] = value["component_configuration"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeComponentConfigurationRecommendationResponse:
    out: DescribeComponentConfigurationRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "ComponentConfiguration" in data:
        out["component_configuration"] = data["ComponentConfiguration"]
    return out
