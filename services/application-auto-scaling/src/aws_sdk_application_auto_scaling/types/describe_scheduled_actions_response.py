"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#DescribeScheduledActionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.scheduled_actions
    import aws_sdk_application_auto_scaling.types.xml_string


class DescribeScheduledActionsResponse(TypedDict):
    scheduled_actions: NotRequired[
        "aws_sdk_application_auto_scaling.types.scheduled_actions.ScheduledActions"
    ]
    """<p>Information about the scheduled actions.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_auto_scaling.types.xml_string.XmlString"
    ]
    """<p>The token required to get the next set of results. This value is <code>null</code> if there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScheduledActionsResponse) -> dict:
    out: dict = {}
    if "scheduled_actions" in value:
        import aws_sdk_application_auto_scaling.types.scheduled_actions

        out["ScheduledActions"] = (
            aws_sdk_application_auto_scaling.types.scheduled_actions.serialize_aws_json_1_1(
                value["scheduled_actions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScheduledActionsResponse:
    out: DescribeScheduledActionsResponse = {}  # type: ignore[typeddict-item]
    if "ScheduledActions" in data:
        import aws_sdk_application_auto_scaling.types.scheduled_actions

        out["scheduled_actions"] = (
            aws_sdk_application_auto_scaling.types.scheduled_actions.deserialize_aws_json_1_1(
                data["ScheduledActions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
