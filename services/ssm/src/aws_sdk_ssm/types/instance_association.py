"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_id
    import aws_sdk_ssm.types.association_version
    import aws_sdk_ssm.types.document_content
    import aws_sdk_ssm.types.instance_id


class InstanceAssociation(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_ssm.types.association_id.AssociationId"]
    """<p>The association ID.</p>"""
    instance_id: NotRequired["aws_sdk_ssm.types.instance_id.InstanceId"]
    """<p>The managed node ID.</p>"""
    content: NotRequired["aws_sdk_ssm.types.document_content.DocumentContent"]
    """<p>The content of the association document for the managed nodes.</p>"""
    association_version: NotRequired[
        "aws_sdk_ssm.types.association_version.AssociationVersion"
    ]
    """<p>Version information for the association on the managed node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAssociation) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAssociation:
    out: InstanceAssociation = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "AssociationVersion" in data:
        out["association_version"] = data["AssociationVersion"]
    return out
