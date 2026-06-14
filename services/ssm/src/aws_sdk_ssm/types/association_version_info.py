"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationVersionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.apply_only_at_cron_interval
    import aws_sdk_ssm.types.association_compliance_severity
    import aws_sdk_ssm.types.association_dispatch_assume_role_arn
    import aws_sdk_ssm.types.association_id
    import aws_sdk_ssm.types.association_name
    import aws_sdk_ssm.types.association_sync_compliance
    import aws_sdk_ssm.types.association_version
    import aws_sdk_ssm.types.calendar_name_or_arn_list
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.duration
    import aws_sdk_ssm.types.instance_association_output_location
    import aws_sdk_ssm.types.max_concurrency
    import aws_sdk_ssm.types.max_errors
    import aws_sdk_ssm.types.parameters
    import aws_sdk_ssm.types.schedule_expression
    import aws_sdk_ssm.types.schedule_offset
    import aws_sdk_ssm.types.target_locations
    import aws_sdk_ssm.types.target_maps
    import aws_sdk_ssm.types.targets


class AssociationVersionInfo(TypedDict):
    association_id: NotRequired["aws_sdk_ssm.types.association_id.AssociationId"]
    """<p>The ID created by the system when the association was created.</p>"""
    association_version: NotRequired[
        "aws_sdk_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The association version.</p>"""
    created_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date the association version was created.</p>"""
    name: NotRequired["aws_sdk_ssm.types.document_arn.DocumentARN"]
    """<p>The name specified when the association was created.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The version of an Amazon Web Services Systems Manager document (SSM document) used when the association version was created.</p>"""
    parameters: NotRequired["aws_sdk_ssm.types.parameters.Parameters"]
    """<p>Parameters specified when the association version was created.</p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>The targets specified for the association when the association version was created. </p>"""
    schedule_expression: NotRequired[
        "aws_sdk_ssm.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The cron or rate schedule specified for the association when the association version was created.</p>"""
    output_location: NotRequired[
        "aws_sdk_ssm.types.instance_association_output_location.InstanceAssociationOutputLocation"
    ]
    """<p>The location in Amazon S3 specified for the association when the association version was created.</p>"""
    association_name: NotRequired["aws_sdk_ssm.types.association_name.AssociationName"]
    """<p>The name specified for the association version when the association version was created.</p>"""
    max_errors: NotRequired["aws_sdk_ssm.types.max_errors.MaxErrors"]
    """<p>The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set <code>MaxError</code> to 10%, then the system stops sending the request when the sixth error is received.</p> <p>Executions that are already running an association when <code>MaxErrors</code> is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set <code>MaxConcurrency</code> to 1 so that executions proceed one at a time.</p>"""
    max_concurrency: NotRequired["aws_sdk_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.</p> <p>If a new managed node starts and attempts to run an association while Systems Manager is running <code>MaxConcurrency</code> associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for <code>MaxConcurrency</code>.</p>"""
    compliance_severity: NotRequired[
        "aws_sdk_ssm.types.association_compliance_severity.AssociationComplianceSeverity"
    ]
    """<p>The severity level that is assigned to the association.</p>"""
    sync_compliance: NotRequired[
        "aws_sdk_ssm.types.association_sync_compliance.AssociationSyncCompliance"
    ]
    """<p>The mode for generating association compliance. You can specify <code>AUTO</code> or <code>MANUAL</code>. In <code>AUTO</code> mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is <code>COMPLIANT</code>. If the association execution doesn't run successfully, the association is <code>NON-COMPLIANT</code>.</p> <p>In <code>MANUAL</code> mode, you must specify the <code>AssociationId</code> as a parameter for the <a>PutComplianceItems</a> API operation. In this case, compliance data isn't managed by State Manager, a tool in Amazon Web Services Systems Manager. It is managed by your direct call to the <a>PutComplianceItems</a> API operation.</p> <p>By default, all associations use <code>AUTO</code> mode.</p>"""
    apply_only_at_cron_interval: (
        "aws_sdk_ssm.types.apply_only_at_cron_interval.ApplyOnlyAtCronInterval"
    )
    """<p>By default, when you create new associations, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you don't want an association to run immediately after you create it. This parameter isn't supported for rate expressions.</p>"""
    calendar_names: NotRequired[
        "aws_sdk_ssm.types.calendar_name_or_arn_list.CalendarNameOrARNList"
    ]
    r"""<p>The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations for this version only run when that Change Calendar is open. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar\">Amazon Web Services Systems Manager Change Calendar</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    target_locations: NotRequired["aws_sdk_ssm.types.target_locations.TargetLocations"]
    """<p>The combination of Amazon Web Services Regions and Amazon Web Services accounts where you wanted to run the association when this association version was created.</p>"""
    schedule_offset: NotRequired["aws_sdk_ssm.types.schedule_offset.ScheduleOffset"]
    """<p>Number of days to wait after the scheduled day to run an association.</p>"""
    duration: NotRequired["aws_sdk_ssm.types.duration.Duration"]
    """<p>The number of hours that an association can run on specified targets. After the resulting cutoff time passes, associations that are currently running are cancelled, and no pending executions are started on remaining targets.</p>"""
    target_maps: NotRequired["aws_sdk_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""
    association_dispatch_assume_role: NotRequired[
        "aws_sdk_ssm.types.association_dispatch_assume_role_arn.AssociationDispatchAssumeRoleArn"
    ]
    r"""<p>A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html\"> service-linked role for Systems Manager</a> will be used by default. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationVersionInfo) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    if "created_date" in value:
        import aws_sdk_ssm.types.date_time

        out["CreatedDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "parameters" in value:
        import aws_sdk_ssm.types.parameters

        out["Parameters"] = aws_sdk_ssm.types.parameters.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "targets" in value:
        import aws_sdk_ssm.types.targets

        out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "output_location" in value:
        import aws_sdk_ssm.types.instance_association_output_location

        out["OutputLocation"] = (
            aws_sdk_ssm.types.instance_association_output_location.serialize_aws_json_1_1(
                value["output_location"]
            )
        )
    if "association_name" in value:
        out["AssociationName"] = value["association_name"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "compliance_severity" in value:
        import aws_sdk_ssm.types.association_compliance_severity

        out["ComplianceSeverity"] = (
            aws_sdk_ssm.types.association_compliance_severity.serialize_aws_json_1_1(
                value["compliance_severity"]
            )
        )
    if "sync_compliance" in value:
        import aws_sdk_ssm.types.association_sync_compliance

        out["SyncCompliance"] = (
            aws_sdk_ssm.types.association_sync_compliance.serialize_aws_json_1_1(
                value["sync_compliance"]
            )
        )
    out["ApplyOnlyAtCronInterval"] = value.get("apply_only_at_cron_interval", False)
    if "calendar_names" in value:
        import aws_sdk_ssm.types.calendar_name_or_arn_list

        out["CalendarNames"] = (
            aws_sdk_ssm.types.calendar_name_or_arn_list.serialize_aws_json_1_1(
                value["calendar_names"]
            )
        )
    if "target_locations" in value:
        import aws_sdk_ssm.types.target_locations

        out["TargetLocations"] = (
            aws_sdk_ssm.types.target_locations.serialize_aws_json_1_1(
                value["target_locations"]
            )
        )
    if "schedule_offset" in value:
        out["ScheduleOffset"] = value["schedule_offset"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "target_maps" in value:
        import aws_sdk_ssm.types.target_maps

        out["TargetMaps"] = aws_sdk_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "association_dispatch_assume_role" in value:
        out["AssociationDispatchAssumeRole"] = value["association_dispatch_assume_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationVersionInfo:
    out: AssociationVersionInfo = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "AssociationVersion" in data:
        out["association_version"] = data["AssociationVersion"]
    if "CreatedDate" in data:
        import aws_sdk_ssm.types.date_time

        out["created_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "Parameters" in data:
        import aws_sdk_ssm.types.parameters

        out["parameters"] = aws_sdk_ssm.types.parameters.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    if "OutputLocation" in data:
        import aws_sdk_ssm.types.instance_association_output_location

        out["output_location"] = (
            aws_sdk_ssm.types.instance_association_output_location.deserialize_aws_json_1_1(
                data["OutputLocation"]
            )
        )
    if "AssociationName" in data:
        out["association_name"] = data["AssociationName"]
    if "MaxErrors" in data:
        out["max_errors"] = data["MaxErrors"]
    if "MaxConcurrency" in data:
        out["max_concurrency"] = data["MaxConcurrency"]
    if "ComplianceSeverity" in data:
        import aws_sdk_ssm.types.association_compliance_severity

        out["compliance_severity"] = (
            aws_sdk_ssm.types.association_compliance_severity.deserialize_aws_json_1_1(
                data["ComplianceSeverity"]
            )
        )
    if "SyncCompliance" in data:
        import aws_sdk_ssm.types.association_sync_compliance

        out["sync_compliance"] = (
            aws_sdk_ssm.types.association_sync_compliance.deserialize_aws_json_1_1(
                data["SyncCompliance"]
            )
        )
    if "ApplyOnlyAtCronInterval" in data:
        out["apply_only_at_cron_interval"] = data["ApplyOnlyAtCronInterval"]
    else:
        out["apply_only_at_cron_interval"] = False
    if "CalendarNames" in data:
        import aws_sdk_ssm.types.calendar_name_or_arn_list

        out["calendar_names"] = (
            aws_sdk_ssm.types.calendar_name_or_arn_list.deserialize_aws_json_1_1(
                data["CalendarNames"]
            )
        )
    if "TargetLocations" in data:
        import aws_sdk_ssm.types.target_locations

        out["target_locations"] = (
            aws_sdk_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    if "ScheduleOffset" in data:
        out["schedule_offset"] = data["ScheduleOffset"]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "TargetMaps" in data:
        import aws_sdk_ssm.types.target_maps

        out["target_maps"] = aws_sdk_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if "AssociationDispatchAssumeRole" in data:
        out["association_dispatch_assume_role"] = data["AssociationDispatchAssumeRole"]
    return out
