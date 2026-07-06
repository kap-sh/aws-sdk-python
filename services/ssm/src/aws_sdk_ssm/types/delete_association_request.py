"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_id
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.instance_id


class DeleteAssociationRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the SSM document.</p>"""
    instance_id: NotRequired["aws_sdk_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID.</p> <note> <p> <code>InstanceId</code> has been deprecated. To specify a managed node ID for an association, use the <code>Targets</code> parameter. Requests that include the parameter <code>InstanceID</code> with Systems Manager documents (SSM documents) that use schema version 2.0 or later will fail. In addition, if you use the parameter <code>InstanceId</code>, you can't use the parameters <code>AssociationName</code>, <code>DocumentVersion</code>, <code>MaxErrors</code>, <code>MaxConcurrency</code>, <code>OutputLocation</code>, or <code>ScheduleExpression</code>. To use these parameters, you must use the <code>Targets</code> parameter.</p> </note>"""
    association_id: NotRequired["aws_sdk_ssm.types.association_id.AssociationId"]
    """<p>The association ID that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAssociationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAssociationRequest:
    out: DeleteAssociationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    return out
