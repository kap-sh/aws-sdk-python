"""Generated from Smithy shape ``com.amazonaws.ssm#TargetLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.accounts
    import aws_sdk_ssm.types.alarm_configuration
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.exclude_accounts
    import aws_sdk_ssm.types.execution_role_name
    import aws_sdk_ssm.types.max_concurrency
    import aws_sdk_ssm.types.max_errors
    import aws_sdk_ssm.types.regions
    import aws_sdk_ssm.types.targets


class TargetLocation(TypedDict, closed=True):
    accounts: NotRequired["aws_sdk_ssm.types.accounts.Accounts"]
    """<p>The Amazon Web Services accounts targeted by the current Automation execution.</p>"""
    regions: NotRequired["aws_sdk_ssm.types.regions.Regions"]
    """<p>The Amazon Web Services Regions targeted by the current Automation execution.</p>"""
    target_location_max_concurrency: NotRequired[
        "aws_sdk_ssm.types.max_concurrency.MaxConcurrency"
    ]
    """<p>The maximum number of Amazon Web Services Regions and Amazon Web Services accounts allowed to run the Automation concurrently. <code>TargetLocationMaxConcurrency</code> has a default value of 1.</p>"""
    target_location_max_errors: NotRequired["aws_sdk_ssm.types.max_errors.MaxErrors"]
    """<p>The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation. <code>TargetLocationMaxErrors</code> has a default value of 0.</p>"""
    execution_role_name: NotRequired[
        "aws_sdk_ssm.types.execution_role_name.ExecutionRoleName"
    ]
    """<p>The Automation execution role used by the currently running Automation. If not specified, the default value is <code>AWS-SystemsManager-AutomationExecutionRole</code>.</p>"""
    target_location_alarm_configuration: NotRequired[
        "aws_sdk_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    include_child_organization_units: "aws_sdk_ssm.types.boolean.Boolean"
    """<p>Indicates whether to include child organizational units (OUs) that are children of the targeted OUs. The default is <code>false</code>.</p> <note> <p>This parameter is not supported by State Manager.</p> </note>"""
    exclude_accounts: NotRequired["aws_sdk_ssm.types.exclude_accounts.ExcludeAccounts"]
    """<p>Amazon Web Services accounts or organizational units to exclude as expanded targets.</p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>A list of key-value mappings to target resources. If you specify values for this data type, you must also specify a value for <code>TargetParameterName</code>.</p> <p>This <code>Targets</code> parameter takes precedence over the <code>StartAutomationExecution:Targets</code> parameter if both are supplied.</p>"""
    targets_max_concurrency: NotRequired[
        "aws_sdk_ssm.types.max_concurrency.MaxConcurrency"
    ]
    """<p>The maximum number of targets allowed to run this task in parallel. This <code>TargetsMaxConcurrency</code> takes precedence over the <code>StartAutomationExecution:MaxConcurrency</code> parameter if both are supplied.</p>"""
    targets_max_errors: NotRequired["aws_sdk_ssm.types.max_errors.MaxErrors"]
    """<p>The maximum number of errors that are allowed before the system stops running the automation on additional targets. This <code>TargetsMaxErrors</code> parameter takes precedence over the <code>StartAutomationExecution:MaxErrors</code> parameter if both are supplied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetLocation) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_ssm.types.accounts

        out["Accounts"] = aws_sdk_ssm.types.accounts.serialize_aws_json_1_1(
            value["accounts"]
        )
    if "regions" in value:
        import aws_sdk_ssm.types.regions

        out["Regions"] = aws_sdk_ssm.types.regions.serialize_aws_json_1_1(
            value["regions"]
        )
    if "target_location_max_concurrency" in value:
        out["TargetLocationMaxConcurrency"] = value["target_location_max_concurrency"]
    if "target_location_max_errors" in value:
        out["TargetLocationMaxErrors"] = value["target_location_max_errors"]
    if "execution_role_name" in value:
        out["ExecutionRoleName"] = value["execution_role_name"]
    if "target_location_alarm_configuration" in value:
        import aws_sdk_ssm.types.alarm_configuration

        out["TargetLocationAlarmConfiguration"] = (
            aws_sdk_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["target_location_alarm_configuration"]
            )
        )
    out["IncludeChildOrganizationUnits"] = value.get(
        "include_child_organization_units", False
    )
    if "exclude_accounts" in value:
        import aws_sdk_ssm.types.exclude_accounts

        out["ExcludeAccounts"] = (
            aws_sdk_ssm.types.exclude_accounts.serialize_aws_json_1_1(
                value["exclude_accounts"]
            )
        )
    if "targets" in value:
        import aws_sdk_ssm.types.targets

        out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "targets_max_concurrency" in value:
        out["TargetsMaxConcurrency"] = value["targets_max_concurrency"]
    if "targets_max_errors" in value:
        out["TargetsMaxErrors"] = value["targets_max_errors"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetLocation:
    out: TargetLocation = {}  # type: ignore[typeddict-item]
    if "Accounts" in data:
        import aws_sdk_ssm.types.accounts

        out["accounts"] = aws_sdk_ssm.types.accounts.deserialize_aws_json_1_1(
            data["Accounts"]
        )
    if "Regions" in data:
        import aws_sdk_ssm.types.regions

        out["regions"] = aws_sdk_ssm.types.regions.deserialize_aws_json_1_1(
            data["Regions"]
        )
    if "TargetLocationMaxConcurrency" in data:
        out["target_location_max_concurrency"] = data["TargetLocationMaxConcurrency"]
    if "TargetLocationMaxErrors" in data:
        out["target_location_max_errors"] = data["TargetLocationMaxErrors"]
    if "ExecutionRoleName" in data:
        out["execution_role_name"] = data["ExecutionRoleName"]
    if "TargetLocationAlarmConfiguration" in data:
        import aws_sdk_ssm.types.alarm_configuration

        out["target_location_alarm_configuration"] = (
            aws_sdk_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["TargetLocationAlarmConfiguration"]
            )
        )
    if "IncludeChildOrganizationUnits" in data:
        out["include_child_organization_units"] = data["IncludeChildOrganizationUnits"]
    else:
        out["include_child_organization_units"] = False
    if "ExcludeAccounts" in data:
        import aws_sdk_ssm.types.exclude_accounts

        out["exclude_accounts"] = (
            aws_sdk_ssm.types.exclude_accounts.deserialize_aws_json_1_1(
                data["ExcludeAccounts"]
            )
        )
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "TargetsMaxConcurrency" in data:
        out["targets_max_concurrency"] = data["TargetsMaxConcurrency"]
    if "TargetsMaxErrors" in data:
        out["targets_max_errors"] = data["TargetsMaxErrors"]
    return out
