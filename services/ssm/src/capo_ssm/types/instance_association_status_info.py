"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociationStatusInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.agent_error_code
    import capo_ssm.types.association_id
    import capo_ssm.types.association_name
    import capo_ssm.types.association_version
    import capo_ssm.types.date_time
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.instance_association_execution_summary
    import capo_ssm.types.instance_association_output_url
    import capo_ssm.types.instance_id
    import capo_ssm.types.status_name


class InstanceAssociationStatusInfo(TypedDict, closed=True):
    association_id: NotRequired["capo_ssm.types.association_id.AssociationId"]
    """<p>The association ID.</p>"""
    name: NotRequired["capo_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the association.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The association document versions.</p>"""
    association_version: NotRequired[
        "capo_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The version of the association applied to the managed node.</p>"""
    instance_id: NotRequired["capo_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID where the association was created.</p>"""
    execution_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the association ran. </p>"""
    status: NotRequired["capo_ssm.types.status_name.StatusName"]
    """<p>Status information about the association.</p>"""
    detailed_status: NotRequired["capo_ssm.types.status_name.StatusName"]
    """<p>Detailed status information about the association.</p>"""
    execution_summary: NotRequired[
        "capo_ssm.types.instance_association_execution_summary.InstanceAssociationExecutionSummary"
    ]
    """<p>Summary information about association execution.</p>"""
    error_code: NotRequired["capo_ssm.types.agent_error_code.AgentErrorCode"]
    """<p>An error code returned by the request to create the association.</p>"""
    output_url: NotRequired[
        "capo_ssm.types.instance_association_output_url.InstanceAssociationOutputUrl"
    ]
    """<p>A URL for an S3 bucket where you want to store the results of this request.</p>"""
    association_name: NotRequired["capo_ssm.types.association_name.AssociationName"]
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
        import capo_ssm.types.date_time

        out["ExecutionDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
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
        import capo_ssm.types.instance_association_output_url

        out["OutputUrl"] = (
            capo_ssm.types.instance_association_output_url.serialize_aws_json_1_1(
                value["output_url"]
            )
        )
    if "association_name" in value:
        out["AssociationName"] = value["association_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAssociationStatusInfo:
    out: InstanceAssociationStatusInfo = {}  # type: ignore[typeddict-item]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("AssociationVersion") is not None:
        out["association_version"] = data["AssociationVersion"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ExecutionDate") is not None:
        import capo_ssm.types.date_time

        out["execution_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExecutionDate"]
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("DetailedStatus") is not None:
        out["detailed_status"] = data["DetailedStatus"]
    if data.get("ExecutionSummary") is not None:
        out["execution_summary"] = data["ExecutionSummary"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("OutputUrl") is not None:
        import capo_ssm.types.instance_association_output_url

        out["output_url"] = (
            capo_ssm.types.instance_association_output_url.deserialize_aws_json_1_1(
                data["OutputUrl"]
            )
        )
    if data.get("AssociationName") is not None:
        out["association_name"] = data["AssociationName"]
    return out
