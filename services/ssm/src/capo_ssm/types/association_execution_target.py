"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_execution_id
    import capo_ssm.types.association_id
    import capo_ssm.types.association_resource_id
    import capo_ssm.types.association_resource_type
    import capo_ssm.types.association_version
    import capo_ssm.types.date_time
    import capo_ssm.types.output_source
    import capo_ssm.types.status_name


class AssociationExecutionTarget(TypedDict, closed=True):
    association_id: NotRequired["capo_ssm.types.association_id.AssociationId"]
    """<p>The association ID.</p>"""
    association_version: NotRequired[
        "capo_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The association version.</p>"""
    execution_id: NotRequired[
        "capo_ssm.types.association_execution_id.AssociationExecutionId"
    ]
    """<p>The execution ID.</p>"""
    resource_id: NotRequired[
        "capo_ssm.types.association_resource_id.AssociationResourceId"
    ]
    """<p>The resource ID, for example, the managed node ID where the association ran.</p>"""
    resource_type: NotRequired[
        "capo_ssm.types.association_resource_type.AssociationResourceType"
    ]
    """<p>The resource type, for example, EC2.</p>"""
    status: NotRequired["capo_ssm.types.status_name.StatusName"]
    """<p>The association execution status.</p>"""
    detailed_status: NotRequired["capo_ssm.types.status_name.StatusName"]
    """<p>Detailed information about the execution status.</p>"""
    last_execution_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date of the last execution.</p>"""
    output_source: NotRequired["capo_ssm.types.output_source.OutputSource"]
    """<p>The location where the association details are saved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionTarget) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "status" in value:
        out["Status"] = value["status"]
    if "detailed_status" in value:
        out["DetailedStatus"] = value["detailed_status"]
    if "last_execution_date" in value:
        import capo_ssm.types.date_time

        out["LastExecutionDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_execution_date"]
        )
    if "output_source" in value:
        import capo_ssm.types.output_source

        out["OutputSource"] = capo_ssm.types.output_source.serialize_aws_json_1_1(
            value["output_source"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationExecutionTarget:
    out: AssociationExecutionTarget = {}  # type: ignore[typeddict-item]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("AssociationVersion") is not None:
        out["association_version"] = data["AssociationVersion"]
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("DetailedStatus") is not None:
        out["detailed_status"] = data["DetailedStatus"]
    if data.get("LastExecutionDate") is not None:
        import capo_ssm.types.date_time

        out["last_execution_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastExecutionDate"]
        )
    if data.get("OutputSource") is not None:
        import capo_ssm.types.output_source

        out["output_source"] = capo_ssm.types.output_source.deserialize_aws_json_1_1(
            data["OutputSource"]
        )
    return out
