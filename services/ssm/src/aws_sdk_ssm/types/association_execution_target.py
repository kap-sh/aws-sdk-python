"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_execution_id
    import aws_sdk_ssm.types.association_id
    import aws_sdk_ssm.types.association_resource_id
    import aws_sdk_ssm.types.association_resource_type
    import aws_sdk_ssm.types.association_version
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.output_source
    import aws_sdk_ssm.types.status_name


class AssociationExecutionTarget(TypedDict):
    association_id: NotRequired["aws_sdk_ssm.types.association_id.AssociationId"]
    """<p>The association ID.</p>"""
    association_version: NotRequired[
        "aws_sdk_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The association version.</p>"""
    execution_id: NotRequired[
        "aws_sdk_ssm.types.association_execution_id.AssociationExecutionId"
    ]
    """<p>The execution ID.</p>"""
    resource_id: NotRequired[
        "aws_sdk_ssm.types.association_resource_id.AssociationResourceId"
    ]
    """<p>The resource ID, for example, the managed node ID where the association ran.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ssm.types.association_resource_type.AssociationResourceType"
    ]
    """<p>The resource type, for example, EC2.</p>"""
    status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>The association execution status.</p>"""
    detailed_status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>Detailed information about the execution status.</p>"""
    last_execution_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date of the last execution.</p>"""
    output_source: NotRequired["aws_sdk_ssm.types.output_source.OutputSource"]
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
        import aws_sdk_ssm.types.date_time

        out["LastExecutionDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_execution_date"]
        )
    if "output_source" in value:
        import aws_sdk_ssm.types.output_source

        out["OutputSource"] = aws_sdk_ssm.types.output_source.serialize_aws_json_1_1(
            value["output_source"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationExecutionTarget:
    out: AssociationExecutionTarget = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "AssociationVersion" in data:
        out["association_version"] = data["AssociationVersion"]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "DetailedStatus" in data:
        out["detailed_status"] = data["DetailedStatus"]
    if "LastExecutionDate" in data:
        import aws_sdk_ssm.types.date_time

        out["last_execution_date"] = (
            aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
                data["LastExecutionDate"]
            )
        )
    if "OutputSource" in data:
        import aws_sdk_ssm.types.output_source

        out["output_source"] = aws_sdk_ssm.types.output_source.deserialize_aws_json_1_1(
            data["OutputSource"]
        )
    return out
