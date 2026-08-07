"""Generated from Smithy shape ``com.amazonaws.docdb#DBSubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.network_type_list
    import capo_docdb.types.string
    import capo_docdb.types.subnet_list


class DBSubnetGroup(TypedDict, closed=True):
    db_subnet_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the subnet group.</p>"""
    db_subnet_group_description: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the description of the subnet group.</p>"""
    vpc_id: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the virtual private cloud (VPC) ID of the subnet group.</p>"""
    subnet_group_status: NotRequired["capo_docdb.types.string.String"]
    """<p>Provides the status of the subnet group.</p>"""
    subnets: NotRequired["capo_docdb.types.subnet_list.SubnetList"]
    """<p>Detailed information about one or more subnets within a subnet group.</p>"""
    db_subnet_group_arn: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB subnet group.</p>"""
    supported_network_types: NotRequired[
        "capo_docdb.types.network_type_list.NetworkTypeList"
    ]
    """<p>The network type of the DB subnet group.</p> <p>Valid Values: <code>IPV4</code> | <code>DUAL</code> </p> <p>A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (DUAL).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "db_subnet_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}DBSubnetGroupDescription",
                str(value["db_subnet_group_description"]),
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "subnet_group_status" in value:
        pairs.append(
            (f"{key_prefix}SubnetGroupStatus", str(value["subnet_group_status"]))
        )
    if "subnets" in value:
        import capo_docdb.types.subnet_list

        capo_docdb.types.subnet_list.serialize_query(
            value["subnets"], pairs, f"{key_prefix}Subnets"
        )
    if "db_subnet_group_arn" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupArn", str(value["db_subnet_group_arn"]))
        )
    if "supported_network_types" in value:
        import capo_docdb.types.network_type_list

        capo_docdb.types.network_type_list.serialize_query(
            value["supported_network_types"],
            pairs,
            f"{key_prefix}SupportedNetworkTypes",
        )


def deserialize_query(el: Element) -> DBSubnetGroup:
    out: DBSubnetGroup = {}  # type: ignore[typeddict-item]
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_db_subnet_group_description = el.find("DBSubnetGroupDescription")
    if child_db_subnet_group_description is not None:
        out["db_subnet_group_description"] = str(
            child_db_subnet_group_description.text or ""
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_group_status = el.find("SubnetGroupStatus")
    if child_subnet_group_status is not None:
        out["subnet_group_status"] = str(child_subnet_group_status.text or "")
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_docdb.types.subnet_list

        out["subnets"] = capo_docdb.types.subnet_list.deserialize_query(child_subnets)
    child_db_subnet_group_arn = el.find("DBSubnetGroupArn")
    if child_db_subnet_group_arn is not None:
        out["db_subnet_group_arn"] = str(child_db_subnet_group_arn.text or "")
    child_supported_network_types = el.find("SupportedNetworkTypes")
    if child_supported_network_types is not None:
        import capo_docdb.types.network_type_list

        out["supported_network_types"] = (
            capo_docdb.types.network_type_list.deserialize_query(
                child_supported_network_types
            )
        )
    return out
