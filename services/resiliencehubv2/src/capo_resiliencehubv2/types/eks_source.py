"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.eks_namespace_list


class EksSource(TypedDict, closed=True):
    cluster_arn: "capo_resiliencehubv2.types.arn.Arn"
    namespaces: "capo_resiliencehubv2.types.eks_namespace_list.EksNamespaceList"
    """<p>The list of Kubernetes namespaces within the EKS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksSource) -> dict:
    out: dict = {}
    out["clusterArn"] = value["cluster_arn"]
    import capo_resiliencehubv2.types.eks_namespace_list

    out["namespaces"] = capo_resiliencehubv2.types.eks_namespace_list.serialize_json(
        value["namespaces"]
    )
    return out


def deserialize_json(data: dict) -> EksSource:
    out: EksSource = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("EksSource.cluster_arn required")
    if "namespaces" in data:
        import capo_resiliencehubv2.types.eks_namespace_list

        out["namespaces"] = (
            capo_resiliencehubv2.types.eks_namespace_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        raise DeserializationError("EksSource.namespaces required")
    return out
