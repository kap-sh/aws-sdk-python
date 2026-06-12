"""Generated from Smithy shape ``com.amazonaws.redshift#CreateClusterSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.subnet_identifier_list
    import aws_sdk_redshift.types.tag_list


class CreateClusterSubnetGroupMessage(TypedDict):
    cluster_subnet_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name for the subnet group. Amazon Redshift stores the value as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain no more than 255 alphanumeric characters or hyphens.</p> </li> <li> <p>Must not be \"Default\".</p> </li> <li> <p>Must be unique for all subnet groups that are created by your Amazon Web Services account.</p> </li> </ul> <p>Example: <code>examplesubnetgroup</code> </p>"""
    description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A description for the subnet group.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_redshift.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.</p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateClusterSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
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
        import aws_sdk_redshift.types.subnet_identifier_list

        aws_sdk_redshift.types.subnet_identifier_list.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateClusterSubnetGroupMessage:
    out: CreateClusterSubnetGroupMessage = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_redshift.types.subnet_identifier_list

        out["subnet_ids"] = (
            aws_sdk_redshift.types.subnet_identifier_list.deserialize_query(
                child_subnet_ids
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    return out
