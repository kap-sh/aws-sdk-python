"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppInputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.eks_source_cluster_namespace
    import capo_resiliencehub.types.integer
    import capo_resiliencehub.types.resource_mapping_type
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.terraform_source


class AppInputSource(TypedDict, closed=True):
    source_name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>The name of the input source.</p>"""
    import_type: "capo_resiliencehub.types.resource_mapping_type.ResourceMappingType"
    """<p>The resource type of the input source.</p>"""
    source_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    r"""<p>The Amazon Resource Name (ARN) of the input source. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    terraform_source: NotRequired[
        "capo_resiliencehub.types.terraform_source.TerraformSource"
    ]
    """<p>The name of the Terraform s3 state ﬁle.</p>"""
    resource_count: "capo_resiliencehub.types.integer.Integer"
    """<p>The number of resources.</p>"""
    eks_source_cluster_namespace: NotRequired[
        "capo_resiliencehub.types.eks_source_cluster_namespace.EksSourceClusterNamespace"
    ]
    """<p>The namespace on your Amazon Elastic Kubernetes Service cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInputSource) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    import capo_resiliencehub.types.resource_mapping_type

    out["importType"] = capo_resiliencehub.types.resource_mapping_type.serialize_json(
        value["import_type"]
    )
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    if "terraform_source" in value:
        import capo_resiliencehub.types.terraform_source

        out["terraformSource"] = (
            capo_resiliencehub.types.terraform_source.serialize_json(
                value["terraform_source"]
            )
        )
    out["resourceCount"] = value.get("resource_count", 0)
    if "eks_source_cluster_namespace" in value:
        import capo_resiliencehub.types.eks_source_cluster_namespace

        out["eksSourceClusterNamespace"] = (
            capo_resiliencehub.types.eks_source_cluster_namespace.serialize_json(
                value["eks_source_cluster_namespace"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppInputSource:
    out: AppInputSource = {}  # type: ignore[typeddict-item]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    if "importType" in data:
        import capo_resiliencehub.types.resource_mapping_type

        out["import_type"] = (
            capo_resiliencehub.types.resource_mapping_type.deserialize_json(
                data["importType"]
            )
        )
    else:
        raise DeserializationError("AppInputSource.import_type required")
    if "sourceArn" in data:
        out["source_arn"] = data["sourceArn"]
    if "terraformSource" in data:
        import capo_resiliencehub.types.terraform_source

        out["terraform_source"] = (
            capo_resiliencehub.types.terraform_source.deserialize_json(
                data["terraformSource"]
            )
        )
    if "resourceCount" in data:
        out["resource_count"] = data["resourceCount"]
    else:
        out["resource_count"] = 0
    if "eksSourceClusterNamespace" in data:
        import capo_resiliencehub.types.eks_source_cluster_namespace

        out["eks_source_cluster_namespace"] = (
            capo_resiliencehub.types.eks_source_cluster_namespace.deserialize_json(
                data["eksSourceClusterNamespace"]
            )
        )
    return out
