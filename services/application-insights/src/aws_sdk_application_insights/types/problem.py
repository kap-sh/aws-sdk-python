"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Problem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.affected_resource
    import aws_sdk_application_insights.types.end_time
    import aws_sdk_application_insights.types.feedback
    import aws_sdk_application_insights.types.insights
    import aws_sdk_application_insights.types.last_recurrence_time
    import aws_sdk_application_insights.types.problem_id
    import aws_sdk_application_insights.types.recurring_count
    import aws_sdk_application_insights.types.resolution_method
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.severity_level
    import aws_sdk_application_insights.types.short_name
    import aws_sdk_application_insights.types.start_time
    import aws_sdk_application_insights.types.status
    import aws_sdk_application_insights.types.title
    import aws_sdk_application_insights.types.visibility


class Problem(TypedDict, closed=True):
    id: NotRequired["aws_sdk_application_insights.types.problem_id.ProblemId"]
    """<p>The ID of the problem.</p>"""
    title: NotRequired["aws_sdk_application_insights.types.title.Title"]
    """<p>The name of the problem.</p>"""
    short_name: NotRequired["aws_sdk_application_insights.types.short_name.ShortName"]
    """<p> The short name of the problem associated with the SNS notification. </p>"""
    insights: NotRequired["aws_sdk_application_insights.types.insights.Insights"]
    """<p>A detailed analysis of the problem using machine learning.</p>"""
    status: NotRequired["aws_sdk_application_insights.types.status.Status"]
    """<p>The status of the problem.</p>"""
    affected_resource: NotRequired[
        "aws_sdk_application_insights.types.affected_resource.AffectedResource"
    ]
    """<p>The resource affected by the problem.</p>"""
    start_time: NotRequired["aws_sdk_application_insights.types.start_time.StartTime"]
    """<p>The time when the problem started, in epoch seconds.</p>"""
    end_time: NotRequired["aws_sdk_application_insights.types.end_time.EndTime"]
    """<p>The time when the problem ended, in epoch seconds.</p>"""
    severity_level: NotRequired[
        "aws_sdk_application_insights.types.severity_level.SeverityLevel"
    ]
    """<p>A measure of the level of impact of the problem.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the owner of the resource group affected by the problem.</p>"""
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group affected by the problem.</p>"""
    feedback: NotRequired["aws_sdk_application_insights.types.feedback.Feedback"]
    """<p>Feedback provided by the user about the problem.</p>"""
    recurring_count: NotRequired[
        "aws_sdk_application_insights.types.recurring_count.RecurringCount"
    ]
    """<p> The number of times that the same problem reoccurred after the first time it was resolved. </p>"""
    last_recurrence_time: NotRequired[
        "aws_sdk_application_insights.types.last_recurrence_time.LastRecurrenceTime"
    ]
    """<p> The last time that the problem reoccurred after its last resolution. </p>"""
    visibility: NotRequired["aws_sdk_application_insights.types.visibility.Visibility"]
    """<p>Specifies whether or not you can view the problem. Updates to ignored problems do not generate notifications.</p>"""
    resolution_method: NotRequired[
        "aws_sdk_application_insights.types.resolution_method.ResolutionMethod"
    ]
    """<p>Specifies how the problem was resolved. If the value is <code>AUTOMATIC</code>, the system resolved the problem. If the value is <code>MANUAL</code>, the user resolved the problem. If the value is <code>UNRESOLVED</code>, then the problem is not resolved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Problem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    if "insights" in value:
        out["Insights"] = value["insights"]
    if "status" in value:
        import aws_sdk_application_insights.types.status

        out["Status"] = (
            aws_sdk_application_insights.types.status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "affected_resource" in value:
        out["AffectedResource"] = value["affected_resource"]
    if "start_time" in value:
        import aws_sdk_application_insights.types.start_time

        out["StartTime"] = (
            aws_sdk_application_insights.types.start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_application_insights.types.end_time

        out["EndTime"] = (
            aws_sdk_application_insights.types.end_time.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "severity_level" in value:
        import aws_sdk_application_insights.types.severity_level

        out["SeverityLevel"] = (
            aws_sdk_application_insights.types.severity_level.serialize_aws_json_1_1(
                value["severity_level"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "feedback" in value:
        import aws_sdk_application_insights.types.feedback

        out["Feedback"] = (
            aws_sdk_application_insights.types.feedback.serialize_aws_json_1_1(
                value["feedback"]
            )
        )
    if "recurring_count" in value:
        out["RecurringCount"] = value["recurring_count"]
    if "last_recurrence_time" in value:
        import aws_sdk_application_insights.types.last_recurrence_time

        out["LastRecurrenceTime"] = (
            aws_sdk_application_insights.types.last_recurrence_time.serialize_aws_json_1_1(
                value["last_recurrence_time"]
            )
        )
    if "visibility" in value:
        import aws_sdk_application_insights.types.visibility

        out["Visibility"] = (
            aws_sdk_application_insights.types.visibility.serialize_aws_json_1_1(
                value["visibility"]
            )
        )
    if "resolution_method" in value:
        import aws_sdk_application_insights.types.resolution_method

        out["ResolutionMethod"] = (
            aws_sdk_application_insights.types.resolution_method.serialize_aws_json_1_1(
                value["resolution_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Problem:
    out: Problem = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "ShortName" in data:
        out["short_name"] = data["ShortName"]
    if "Insights" in data:
        out["insights"] = data["Insights"]
    if "Status" in data:
        import aws_sdk_application_insights.types.status

        out["status"] = (
            aws_sdk_application_insights.types.status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "AffectedResource" in data:
        out["affected_resource"] = data["AffectedResource"]
    if "StartTime" in data:
        import aws_sdk_application_insights.types.start_time

        out["start_time"] = (
            aws_sdk_application_insights.types.start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_application_insights.types.end_time

        out["end_time"] = (
            aws_sdk_application_insights.types.end_time.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if "SeverityLevel" in data:
        import aws_sdk_application_insights.types.severity_level

        out["severity_level"] = (
            aws_sdk_application_insights.types.severity_level.deserialize_aws_json_1_1(
                data["SeverityLevel"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "Feedback" in data:
        import aws_sdk_application_insights.types.feedback

        out["feedback"] = (
            aws_sdk_application_insights.types.feedback.deserialize_aws_json_1_1(
                data["Feedback"]
            )
        )
    if "RecurringCount" in data:
        out["recurring_count"] = data["RecurringCount"]
    if "LastRecurrenceTime" in data:
        import aws_sdk_application_insights.types.last_recurrence_time

        out["last_recurrence_time"] = (
            aws_sdk_application_insights.types.last_recurrence_time.deserialize_aws_json_1_1(
                data["LastRecurrenceTime"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_application_insights.types.visibility

        out["visibility"] = (
            aws_sdk_application_insights.types.visibility.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    if "ResolutionMethod" in data:
        import aws_sdk_application_insights.types.resolution_method

        out["resolution_method"] = (
            aws_sdk_application_insights.types.resolution_method.deserialize_aws_json_1_1(
                data["ResolutionMethod"]
            )
        )
    return out
