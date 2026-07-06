"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_id
    import aws_sdk_ssm.types.association_version
    import aws_sdk_ssm.types.document_arn
    import aws_sdk_ssm.types.instance_id


class DescribeAssociationRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ssm.types.document_arn.DocumentARN"]
    """<p>The name of the SSM document.</p>"""
    instance_id: NotRequired["aws_sdk_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID.</p>"""
    association_id: NotRequired["aws_sdk_ssm.types.association_id.AssociationId"]
    """<p>The association ID for which you want information.</p>"""
    association_version: NotRequired[
        "aws_sdk_ssm.types.association_version.AssociationVersion"
    ]
    """<p>Specify the association version to retrieve. To view the latest version, either specify <code>$LATEST</code> for this parameter, or omit this parameter. To view a list of all associations for a managed node, use <a>ListAssociations</a>. To get a list of versions for a specific association, use <a>ListAssociationVersions</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssociationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssociationRequest:
    out: DescribeAssociationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "AssociationVersion" in data:
        out["association_version"] = data["AssociationVersion"]
    return out
