"""Generated from Smithy shape ``com.amazonaws.xray#GroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.insights_configuration
    import aws_sdk_xray.types.string


class GroupSummary(TypedDict, closed=True):
    group_name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The unique case-sensitive name of the group.</p>"""
    group_arn: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The ARN of the group generated based on the GroupName.</p>"""
    filter_expression: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The filter expression defining the parameters to include traces.</p>"""
    insights_configuration: NotRequired[
        "aws_sdk_xray.types.insights_configuration.InsightsConfiguration"
    ]
    """<p>The structure containing configurations related to insights.</p> <ul> <li> <p>The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group.</p> </li> <li> <p>The NotificationsEnabled boolean can be set to true to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummary) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_arn" in value:
        out["GroupARN"] = value["group_arn"]
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    if "insights_configuration" in value:
        import aws_sdk_xray.types.insights_configuration

        out["InsightsConfiguration"] = (
            aws_sdk_xray.types.insights_configuration.serialize_json(
                value["insights_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroupSummary:
    out: GroupSummary = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupARN" in data:
        out["group_arn"] = data["GroupARN"]
    if "FilterExpression" in data:
        out["filter_expression"] = data["FilterExpression"]
    if "InsightsConfiguration" in data:
        import aws_sdk_xray.types.insights_configuration

        out["insights_configuration"] = (
            aws_sdk_xray.types.insights_configuration.deserialize_json(
                data["InsightsConfiguration"]
            )
        )
    return out
