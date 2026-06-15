"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RemoveDraftAppVersionResourceMappingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.entity_name_list
    import aws_sdk_resiliencehub.types.string255_list


class RemoveDraftAppVersionResourceMappingsRequest(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    resource_names: NotRequired[
        "aws_sdk_resiliencehub.types.entity_name_list.EntityNameList"
    ]
    """<p>The names of the resources you want to remove from the resource mappings.</p>"""
    logical_stack_names: NotRequired[
        "aws_sdk_resiliencehub.types.string255_list.String255List"
    ]
    """<p>The names of the CloudFormation stacks you want to remove from the resource mappings.</p>"""
    app_registry_app_names: NotRequired[
        "aws_sdk_resiliencehub.types.entity_name_list.EntityNameList"
    ]
    """<p>The names of the registered applications you want to remove from the resource mappings.</p>"""
    resource_group_names: NotRequired[
        "aws_sdk_resiliencehub.types.entity_name_list.EntityNameList"
    ]
    """<p>The names of the resource groups you want to remove from the resource mappings.</p>"""
    terraform_source_names: NotRequired[
        "aws_sdk_resiliencehub.types.string255_list.String255List"
    ]
    """<p>The names of the Terraform sources you want to remove from the resource mappings.</p>"""
    eks_source_names: NotRequired[
        "aws_sdk_resiliencehub.types.string255_list.String255List"
    ]
    r"""<p>The names of the Amazon Elastic Kubernetes Service clusters and namespaces you want to remove from the resource mappings.</p> <note> <p>This parameter accepts values in \"eks-cluster/namespace\" format.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveDraftAppVersionResourceMappingsRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "resource_names" in value:
        import aws_sdk_resiliencehub.types.entity_name_list

        out["resourceNames"] = (
            aws_sdk_resiliencehub.types.entity_name_list.serialize_json(
                value["resource_names"]
            )
        )
    if "logical_stack_names" in value:
        import aws_sdk_resiliencehub.types.string255_list

        out["logicalStackNames"] = (
            aws_sdk_resiliencehub.types.string255_list.serialize_json(
                value["logical_stack_names"]
            )
        )
    if "app_registry_app_names" in value:
        import aws_sdk_resiliencehub.types.entity_name_list

        out["appRegistryAppNames"] = (
            aws_sdk_resiliencehub.types.entity_name_list.serialize_json(
                value["app_registry_app_names"]
            )
        )
    if "resource_group_names" in value:
        import aws_sdk_resiliencehub.types.entity_name_list

        out["resourceGroupNames"] = (
            aws_sdk_resiliencehub.types.entity_name_list.serialize_json(
                value["resource_group_names"]
            )
        )
    if "terraform_source_names" in value:
        import aws_sdk_resiliencehub.types.string255_list

        out["terraformSourceNames"] = (
            aws_sdk_resiliencehub.types.string255_list.serialize_json(
                value["terraform_source_names"]
            )
        )
    if "eks_source_names" in value:
        import aws_sdk_resiliencehub.types.string255_list

        out["eksSourceNames"] = (
            aws_sdk_resiliencehub.types.string255_list.serialize_json(
                value["eks_source_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoveDraftAppVersionResourceMappingsRequest:
    out: RemoveDraftAppVersionResourceMappingsRequest = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "RemoveDraftAppVersionResourceMappingsRequest.app_arn required"
        )
    if "resourceNames" in data:
        import aws_sdk_resiliencehub.types.entity_name_list

        out["resource_names"] = (
            aws_sdk_resiliencehub.types.entity_name_list.deserialize_json(
                data["resourceNames"]
            )
        )
    if "logicalStackNames" in data:
        import aws_sdk_resiliencehub.types.string255_list

        out["logical_stack_names"] = (
            aws_sdk_resiliencehub.types.string255_list.deserialize_json(
                data["logicalStackNames"]
            )
        )
    if "appRegistryAppNames" in data:
        import aws_sdk_resiliencehub.types.entity_name_list

        out["app_registry_app_names"] = (
            aws_sdk_resiliencehub.types.entity_name_list.deserialize_json(
                data["appRegistryAppNames"]
            )
        )
    if "resourceGroupNames" in data:
        import aws_sdk_resiliencehub.types.entity_name_list

        out["resource_group_names"] = (
            aws_sdk_resiliencehub.types.entity_name_list.deserialize_json(
                data["resourceGroupNames"]
            )
        )
    if "terraformSourceNames" in data:
        import aws_sdk_resiliencehub.types.string255_list

        out["terraform_source_names"] = (
            aws_sdk_resiliencehub.types.string255_list.deserialize_json(
                data["terraformSourceNames"]
            )
        )
    if "eksSourceNames" in data:
        import aws_sdk_resiliencehub.types.string255_list

        out["eks_source_names"] = (
            aws_sdk_resiliencehub.types.string255_list.deserialize_json(
                data["eksSourceNames"]
            )
        )
    return out
