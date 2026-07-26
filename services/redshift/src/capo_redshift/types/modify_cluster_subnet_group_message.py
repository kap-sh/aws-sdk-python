"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterSubnetGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.subnet_identifier_list


class ModifyClusterSubnetGroupMessage(TypedDict, closed=True):
    cluster_subnet_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the subnet group to be modified.</p>"""
    description: NotRequired["capo_redshift.types.string.String"]
    """<p>A text description of the subnet group to be modified.</p>"""
    subnet_ids: NotRequired[
        "capo_redshift.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_subnet_group_name" in value:
        pairs.append(
            (
                f"{prefix}.ClusterSubnetGroupName",
                str(value["cluster_subnet_group_name"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "subnet_ids" in value:
        import capo_redshift.types.subnet_identifier_list

        capo_redshift.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )


def deserialize_query(el: Element) -> ModifyClusterSubnetGroupMessage:
    out: ModifyClusterSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_cluster_subnet_group_name = el.find("ClusterSubnetGroupName")
    if child_cluster_subnet_group_name is not None:
        out["cluster_subnet_group_name"] = str(
            child_cluster_subnet_group_name.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import capo_redshift.types.subnet_identifier_list

        out["subnet_ids"] = (
            capo_redshift.types.subnet_identifier_list.deserialize_query(
                child_subnet_ids
            )
        )
    return out
