"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#DescribeScalingActivitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.scaling_activities
    import aws_sdk_application_auto_scaling.types.xml_string


class DescribeScalingActivitiesResponse(TypedDict, closed=True):
    scaling_activities: NotRequired[
        "aws_sdk_application_auto_scaling.types.scaling_activities.ScalingActivities"
    ]
    """<p>A list of scaling activity objects.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_auto_scaling.types.xml_string.XmlString"
    ]
    """<p>The token required to get the next set of results. This value is <code>null</code> if there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingActivitiesResponse) -> dict:
    out: dict = {}
    if "scaling_activities" in value:
        import aws_sdk_application_auto_scaling.types.scaling_activities

        out["ScalingActivities"] = (
            aws_sdk_application_auto_scaling.types.scaling_activities.serialize_aws_json_1_1(
                value["scaling_activities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingActivitiesResponse:
    out: DescribeScalingActivitiesResponse = {}  # type: ignore[typeddict-item]
    if "ScalingActivities" in data:
        import aws_sdk_application_auto_scaling.types.scaling_activities

        out["scaling_activities"] = (
            aws_sdk_application_auto_scaling.types.scaling_activities.deserialize_aws_json_1_1(
                data["ScalingActivities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
