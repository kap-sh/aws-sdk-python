"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ScheduledActionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_redshift_serverless.types.iam_role_arn
    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.next_invocations_list
    import aws_sdk_redshift_serverless.types.schedule
    import aws_sdk_redshift_serverless.types.scheduled_action_name
    import aws_sdk_redshift_serverless.types.state
    import aws_sdk_redshift_serverless.types.target_action


class ScheduledActionResponse(TypedDict):
    scheduled_action_name: NotRequired[
        "aws_sdk_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    ]
    """<p>The name of the scheduled action.</p>"""
    schedule: NotRequired["aws_sdk_redshift_serverless.types.schedule.Schedule"]
    """<p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>\"(0 10 ? * MON *)\"</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions\">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>"""
    scheduled_action_description: NotRequired["str"]
    """<p>The description of the scheduled action.</p>"""
    next_invocations: NotRequired[
        "aws_sdk_redshift_serverless.types.next_invocations_list.NextInvocationsList"
    ]
    """<p>An array of timestamps of when the next scheduled actions will trigger.</p>"""
    role_arn: NotRequired["aws_sdk_redshift_serverless.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href=\"https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html\">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>"""
    state: NotRequired["aws_sdk_redshift_serverless.types.state.State"]
    """<p>The state of the scheduled action.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of </p>"""
    target_action: NotRequired[
        "aws_sdk_redshift_serverless.types.target_action.TargetAction"
    ]
    namespace_name: NotRequired[
        "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.</p>"""
    scheduled_action_uuid: NotRequired["str"]
    """<p>The uuid of the scheduled action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action_name" in value:
        out["scheduledActionName"] = value["scheduled_action_name"]
    if "schedule" in value:
        import aws_sdk_redshift_serverless.types.schedule

        out["schedule"] = (
            aws_sdk_redshift_serverless.types.schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "scheduled_action_description" in value:
        out["scheduledActionDescription"] = value["scheduled_action_description"]
    if "next_invocations" in value:
        import aws_sdk_redshift_serverless.types.next_invocations_list

        out["nextInvocations"] = (
            aws_sdk_redshift_serverless.types.next_invocations_list.serialize_aws_json_1_1(
                value["next_invocations"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "state" in value:
        out["state"] = value["state"]
    if "start_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["startTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "target_action" in value:
        import aws_sdk_redshift_serverless.types.target_action

        out["targetAction"] = (
            aws_sdk_redshift_serverless.types.target_action.serialize_aws_json_1_1(
                value["target_action"]
            )
        )
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "scheduled_action_uuid" in value:
        out["scheduledActionUuid"] = value["scheduled_action_uuid"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledActionResponse:
    out: ScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if "scheduledActionName" in data:
        out["scheduled_action_name"] = data["scheduledActionName"]
    if "schedule" in data:
        import aws_sdk_redshift_serverless.types.schedule

        out["schedule"] = (
            aws_sdk_redshift_serverless.types.schedule.deserialize_aws_json_1_1(
                data["schedule"]
            )
        )
    if "scheduledActionDescription" in data:
        out["scheduled_action_description"] = data["scheduledActionDescription"]
    if "nextInvocations" in data:
        import aws_sdk_redshift_serverless.types.next_invocations_list

        out["next_invocations"] = (
            aws_sdk_redshift_serverless.types.next_invocations_list.deserialize_aws_json_1_1(
                data["nextInvocations"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "state" in data:
        out["state"] = data["state"]
    if "startTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["endTime"]
            )
        )
    if "targetAction" in data:
        import aws_sdk_redshift_serverless.types.target_action

        out["target_action"] = (
            aws_sdk_redshift_serverless.types.target_action.deserialize_aws_json_1_1(
                data["targetAction"]
            )
        )
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "scheduledActionUuid" in data:
        out["scheduled_action_uuid"] = data["scheduledActionUuid"]
    return out
