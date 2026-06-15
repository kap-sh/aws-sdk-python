"""Generated from Smithy shape ``com.amazonaws.resiliencehub#LogicalResourceId``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.string255


class LogicalResourceId(TypedDict):
    identifier: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Identifier of the resource.</p>"""
    logical_stack_name: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>The name of the CloudFormation stack this resource belongs to.</p>"""
    resource_group_name: NotRequired[
        "aws_sdk_resiliencehub.types.entity_name.EntityName"
    ]
    """<p>The name of the resource group that this resource belongs to.</p>"""
    terraform_source_name: NotRequired[
        "aws_sdk_resiliencehub.types.string255.String255"
    ]
    """<p> The name of the Terraform S3 state file this resource belongs to. </p>"""
    eks_source_name: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    r"""<p>Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.</p> <note> <p>This parameter accepts values in \"eks-cluster/namespace\" format.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogicalResourceId) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "logical_stack_name" in value:
        out["logicalStackName"] = value["logical_stack_name"]
    if "resource_group_name" in value:
        out["resourceGroupName"] = value["resource_group_name"]
    if "terraform_source_name" in value:
        out["terraformSourceName"] = value["terraform_source_name"]
    if "eks_source_name" in value:
        out["eksSourceName"] = value["eks_source_name"]
    return out


def deserialize_json(data: dict) -> LogicalResourceId:
    out: LogicalResourceId = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("LogicalResourceId.identifier required")
    if "logicalStackName" in data:
        out["logical_stack_name"] = data["logicalStackName"]
    if "resourceGroupName" in data:
        out["resource_group_name"] = data["resourceGroupName"]
    if "terraformSourceName" in data:
        out["terraform_source_name"] = data["terraformSourceName"]
    if "eksSourceName" in data:
        out["eks_source_name"] = data["eksSourceName"]
    return out
