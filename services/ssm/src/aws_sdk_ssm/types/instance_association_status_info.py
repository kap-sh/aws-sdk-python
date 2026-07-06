"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociationStatusInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.agent_error_code
    import aws_sdk_ssm.types.association_id
    import aws_sdk_ssm.types.association_name
    import aws_sdk_ssm.types.association_version
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.document_version
    import aws_sdk_ssm.types.instance_association_execution_summary
    import aws_sdk_ssm.types.instance_association_output_url
    import aws_sdk_ssm.types.instance_id
    import aws_sdk_ssm.types.status_name


class InstanceAssociationStatusInfo(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_ssm.types.association_id.AssociationId"]
    """<p>The association ID.</p>"""
    name: NotRequired["aws_sdk_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the association.</p>"""
    document_version: NotRequired["aws_sdk_ssm.types.document_version.DocumentVersion"]
    """<p>The association document versions.</p>"""
    association_version: NotRequired[
        "aws_sdk_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The version of the association applied to the managed node.</p>"""
    instance_id: NotRequired["aws_sdk_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID where the association was created.</p>"""
    execution_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date the association ran. </p>"""
    status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>Status information about the association.</p>"""
    detailed_status: NotRequired["aws_sdk_ssm.types.status_name.StatusName"]
    """<p>Detailed status information about the association.</p>"""
    execution_summary: NotRequired[
        "aws_sdk_ssm.types.instance_association_execution_summary.InstanceAssociationExecutionSummary"
    ]
    """<p>Summary information about association execution.</p>"""
    error_code: NotRequired["aws_sdk_ssm.types.agent_error_code.AgentErrorCode"]
    """<p>An error code returned by the request to create the association.</p>"""
    output_url: NotRequired[
        "aws_sdk_ssm.types.instance_association_output_url.InstanceAssociationOutputUrl"
    ]
    """<p>A URL for an S3 bucket where you want to store the results of this request.</p>"""
    association_name: NotRequired["aws_sdk_ssm.types.association_name.AssociationName"]
    """<p>The name of the association applied to the managed node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAssociationStatusInfo) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "execution_date" in value:
        import aws_sdk_ssm.types.date_time

        out["ExecutionDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["execution_date"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "detailed_status" in value:
        out["DetailedStatus"] = value["detailed_status"]
    if "execution_summary" in value:
        out["ExecutionSummary"] = value["execution_summary"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "output_url" in value:
        import aws_sdk_ssm.types.instance_association_output_url

        out["OutputUrl"] = (
            aws_sdk_ssm.types.instance_association_output_url.serialize_aws_json_1_1(
                value["output_url"]
            )
        )
    if "association_name" in value:
        out["AssociationName"] = value["association_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAssociationStatusInfo:
    out: InstanceAssociationStatusInfo = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    if "AssociationVersion" in data:
        out["association_version"] = data["AssociationVersion"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "ExecutionDate" in data:
        import aws_sdk_ssm.types.date_time

        out["execution_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExecutionDate"]
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "DetailedStatus" in data:
        out["detailed_status"] = data["DetailedStatus"]
    if "ExecutionSummary" in data:
        out["execution_summary"] = data["ExecutionSummary"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "OutputUrl" in data:
        import aws_sdk_ssm.types.instance_association_output_url

        out["output_url"] = (
            aws_sdk_ssm.types.instance_association_output_url.deserialize_aws_json_1_1(
                data["OutputUrl"]
            )
        )
    if "AssociationName" in data:
        out["association_name"] = data["AssociationName"]
    return out
