"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_configuration
    import aws_sdk_ssm.types.alarm_state_information_list
    import aws_sdk_ssm.types.association_execution_id
    import aws_sdk_ssm.types.association_id
    import aws_sdk_ssm.types.association_version
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.resource_count_by_status
    import aws_sdk_ssm.types.status_name


class AssociationExecution(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_ssm.types.association_id.AssociationId"]
    """<p>The association ID.</p>"""
    association_version: NotRequired[
        "aws_sdk_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The association version.</p>"""
    execution_id: NotRequired[
        "aws_sdk_ssm.types.association_execution_id.AssociationExecutionId"
    ]
    """<p>The execution ID for the association.</p>"""
    status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>The status of the association execution.</p>"""
    detailed_status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>Detailed status information about the execution.</p>"""
    created_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the execution started.</p>"""
    last_execution_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date of the last execution.</p>"""
    resource_count_by_status: NotRequired[
        "aws_sdk_ssm.types.resource_count_by_status.ResourceCountByStatus"
    ]
    """<p>An aggregate status of the resources in the execution based on the status type.</p>"""
    alarm_configuration: NotRequired[
        "aws_sdk_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    triggered_alarms: NotRequired[
        "aws_sdk_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarms that were invoked by the association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecution) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "detailed_status" in value:
        out["DetailedStatus"] = value["detailed_status"]
    if "created_time" in value:
        import aws_sdk_ssm.types.date_time

        out["CreatedTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "last_execution_date" in value:
        import aws_sdk_ssm.types.date_time

        out["LastExecutionDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_execution_date"]
        )
    if "resource_count_by_status" in value:
        out["ResourceCountByStatus"] = value["resource_count_by_status"]
    if "alarm_configuration" in value:
        import aws_sdk_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            aws_sdk_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import aws_sdk_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            aws_sdk_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationExecution:
    out: AssociationExecution = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "AssociationVersion" in data:
        out["association_version"] = data["AssociationVersion"]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "DetailedStatus" in data:
        out["detailed_status"] = data["DetailedStatus"]
    if "CreatedTime" in data:
        import aws_sdk_ssm.types.date_time

        out["created_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if "LastExecutionDate" in data:
        import aws_sdk_ssm.types.date_time

        out["last_execution_date"] = (
            aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
                data["LastExecutionDate"]
            )
        )
    if "ResourceCountByStatus" in data:
        out["resource_count_by_status"] = data["ResourceCountByStatus"]
    if "AlarmConfiguration" in data:
        import aws_sdk_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            aws_sdk_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if "TriggeredAlarms" in data:
        import aws_sdk_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            aws_sdk_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    return out
