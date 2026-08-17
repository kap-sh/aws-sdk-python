"""Generated from Smithy shape ``com.amazonaws.ssm#Association``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_id
    import capo_ssm.types.association_name
    import capo_ssm.types.association_overview
    import capo_ssm.types.association_version
    import capo_ssm.types.date_time
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.duration
    import capo_ssm.types.instance_id
    import capo_ssm.types.schedule_expression
    import capo_ssm.types.schedule_offset
    import capo_ssm.types.target_maps
    import capo_ssm.types.targets


class Association(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the SSM document.</p>"""
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID.</p>"""
    association_id: NotRequired["capo_ssm.types.association_id.AssociationId"]
    """<p>The ID created by the system when you create an association. An association is a binding between a document and a set of targets with a schedule.</p>"""
    association_version: NotRequired[
        "capo_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The association version.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the document used in the association. If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the <code>apply-only-at-cron-interval</code> parameter.</p> <important> <p>State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the <code>default</code> version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to <code>default</code>.</p> </important>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The managed nodes targeted by the request to create an association. You can target all managed nodes in an Amazon Web Services account by specifying the <code>InstanceIds</code> key with a value of <code>*</code>.</p>"""
    last_execution_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date on which the association was last run.</p>"""
    overview: NotRequired["capo_ssm.types.association_overview.AssociationOverview"]
    """<p>Information about the association.</p>"""
    schedule_expression: NotRequired[
        "capo_ssm.types.schedule_expression.ScheduleExpression"
    ]
    """<p>A cron expression that specifies a schedule when the association runs. The schedule runs in Coordinated Universal Time (UTC).</p>"""
    association_name: NotRequired["capo_ssm.types.association_name.AssociationName"]
    """<p>The association name.</p>"""
    schedule_offset: NotRequired["capo_ssm.types.schedule_offset.ScheduleOffset"]
    """<p>Number of days to wait after the scheduled day to run an association.</p>"""
    duration: NotRequired["capo_ssm.types.duration.Duration"]
    """<p>The number of hours that an association can run on specified targets. After the resulting cutoff time passes, associations that are currently running are cancelled, and no pending executions are started on remaining targets.</p>"""
    target_maps: NotRequired["capo_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Association) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "last_execution_date" in value:
        import capo_ssm.types.date_time

        out["LastExecutionDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_execution_date"]
        )
    if "overview" in value:
        import capo_ssm.types.association_overview

        out["Overview"] = capo_ssm.types.association_overview.serialize_aws_json_1_1(
            value["overview"]
        )
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "association_name" in value:
        out["AssociationName"] = value["association_name"]
    if "schedule_offset" in value:
        out["ScheduleOffset"] = value["schedule_offset"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "target_maps" in value:
        import capo_ssm.types.target_maps

        out["TargetMaps"] = capo_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Association:
    out: Association = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("AssociationVersion") is not None:
        out["association_version"] = data["AssociationVersion"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("LastExecutionDate") is not None:
        import capo_ssm.types.date_time

        out["last_execution_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastExecutionDate"]
        )
    if data.get("Overview") is not None:
        import capo_ssm.types.association_overview

        out["overview"] = capo_ssm.types.association_overview.deserialize_aws_json_1_1(
            data["Overview"]
        )
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("AssociationName") is not None:
        out["association_name"] = data["AssociationName"]
    if data.get("ScheduleOffset") is not None:
        out["schedule_offset"] = data["ScheduleOffset"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("TargetMaps") is not None:
        import capo_ssm.types.target_maps

        out["target_maps"] = capo_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    return out
