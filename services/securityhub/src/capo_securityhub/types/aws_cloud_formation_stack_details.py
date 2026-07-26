"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFormationStackDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_formation_stack_drift_information_details
    import capo_securityhub.types.aws_cloud_formation_stack_outputs_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsCloudFormationStackDetails(TypedDict, closed=True):
    capabilities: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The capabilities allowed in the stack. </p>"""
    creation_time: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The time at which the stack was created. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A user-defined description associated with the stack. </p>"""
    disable_rollback: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Boolean to enable or disable rollback on stack creation failures. </p>"""
    drift_information: NotRequired[
        "capo_securityhub.types.aws_cloud_formation_stack_drift_information_details.AwsCloudFormationStackDriftInformationDetails"
    ]
    """<p>Information about whether a stack's actual configuration differs, or has drifted, from its expected configuration, as defined in the stack template and any values specified as template parameters. </p>"""
    enable_termination_protection: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether termination protection is enabled for the stack. </p>"""
    last_updated_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The time the nested stack was last updated. This field will only be returned if the stack has been updated at least once.</p>"""
    notification_arns: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Amazon SNS topic to which stack-related events are published. </p>"""
    outputs: NotRequired[
        "capo_securityhub.types.aws_cloud_formation_stack_outputs_list.AwsCloudFormationStackOutputsList"
    ]
    """<p>A list of output structures. </p>"""
    role_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of an IAM role that's associated with the stack. </p>"""
    stack_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Unique identifier of the stack. </p>"""
    stack_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name associated with the stack. </p>"""
    stack_status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Current status of the stack. </p>"""
    stack_status_reason: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Success or failure message associated with the stack status. </p>"""
    timeout_in_minutes: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The length of time, in minutes, that CloudFormation waits for the nested stack to reach the <code>CREATE_COMPLETE</code> state. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFormationStackDetails) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Capabilities"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["capabilities"]
            )
        )
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "description" in value:
        out["Description"] = value["description"]
    if "disable_rollback" in value:
        out["DisableRollback"] = value["disable_rollback"]
    if "drift_information" in value:
        import capo_securityhub.types.aws_cloud_formation_stack_drift_information_details

        out["DriftInformation"] = (
            capo_securityhub.types.aws_cloud_formation_stack_drift_information_details.serialize_json(
                value["drift_information"]
            )
        )
    if "enable_termination_protection" in value:
        out["EnableTerminationProtection"] = value["enable_termination_protection"]
    if "last_updated_time" in value:
        out["LastUpdatedTime"] = value["last_updated_time"]
    if "notification_arns" in value:
        import capo_securityhub.types.non_empty_string_list

        out["NotificationArns"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["notification_arns"]
            )
        )
    if "outputs" in value:
        import capo_securityhub.types.aws_cloud_formation_stack_outputs_list

        out["Outputs"] = (
            capo_securityhub.types.aws_cloud_formation_stack_outputs_list.serialize_json(
                value["outputs"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "stack_id" in value:
        out["StackId"] = value["stack_id"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "stack_status" in value:
        out["StackStatus"] = value["stack_status"]
    if "stack_status_reason" in value:
        out["StackStatusReason"] = value["stack_status_reason"]
    if "timeout_in_minutes" in value:
        out["TimeoutInMinutes"] = value["timeout_in_minutes"]
    return out


def deserialize_json(data: dict) -> AwsCloudFormationStackDetails:
    out: AwsCloudFormationStackDetails = {}  # type: ignore[typeddict-item]
    if "Capabilities" in data:
        import capo_securityhub.types.non_empty_string_list

        out["capabilities"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["Capabilities"]
            )
        )
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisableRollback" in data:
        out["disable_rollback"] = data["DisableRollback"]
    if "DriftInformation" in data:
        import capo_securityhub.types.aws_cloud_formation_stack_drift_information_details

        out["drift_information"] = (
            capo_securityhub.types.aws_cloud_formation_stack_drift_information_details.deserialize_json(
                data["DriftInformation"]
            )
        )
    if "EnableTerminationProtection" in data:
        out["enable_termination_protection"] = data["EnableTerminationProtection"]
    if "LastUpdatedTime" in data:
        out["last_updated_time"] = data["LastUpdatedTime"]
    if "NotificationArns" in data:
        import capo_securityhub.types.non_empty_string_list

        out["notification_arns"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["NotificationArns"]
            )
        )
    if "Outputs" in data:
        import capo_securityhub.types.aws_cloud_formation_stack_outputs_list

        out["outputs"] = (
            capo_securityhub.types.aws_cloud_formation_stack_outputs_list.deserialize_json(
                data["Outputs"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "StackId" in data:
        out["stack_id"] = data["StackId"]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "StackStatus" in data:
        out["stack_status"] = data["StackStatus"]
    if "StackStatusReason" in data:
        out["stack_status_reason"] = data["StackStatusReason"]
    if "TimeoutInMinutes" in data:
        out["timeout_in_minutes"] = data["TimeoutInMinutes"]
    return out
