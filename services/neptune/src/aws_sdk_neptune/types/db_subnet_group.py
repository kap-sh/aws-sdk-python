"""Generated from Smithy shape ``com.amazonaws.neptune#DBSubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string
    import aws_sdk_neptune.types.string_list
    import aws_sdk_neptune.types.subnet_list


class DBSubnetGroup(TypedDict, closed=True):
    db_subnet_group_name: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the DB subnet group.</p>"""
    db_subnet_group_description: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Provides the description of the DB subnet group.</p>"""
    vpc_id: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Provides the VpcId of the DB subnet group.</p>"""
    subnet_group_status: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Provides the status of the DB subnet group.</p>"""
    subnets: NotRequired["aws_sdk_neptune.types.subnet_list.SubnetList"]
    """<p> Contains a list of <a>Subnet</a> elements.</p>"""
    db_subnet_group_arn: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB subnet group.</p>"""
    supported_network_types: NotRequired["aws_sdk_neptune.types.string_list.StringList"]
    """<p>The network types supported by the DB subnet group.</p> <p>Valid network types include <code>IPV4</code> and <code>DUAL</code>. A DB subnet group supports <code>DUAL</code> if all subnets in the group have both IPv4 and IPv6 CIDRs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{prefix}.DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "db_subnet_group_description" in value:
        pairs.append(
            (
                f"{prefix}.DBSubnetGroupDescription",
                str(value["db_subnet_group_description"]),
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "subnet_group_status" in value:
        pairs.append((f"{prefix}.SubnetGroupStatus", str(value["subnet_group_status"])))
    if "subnets" in value:
        import aws_sdk_neptune.types.subnet_list

        aws_sdk_neptune.types.subnet_list.serialize_query(
            value["subnets"], pairs, f"{prefix}.Subnets"
        )
    if "db_subnet_group_arn" in value:
        pairs.append((f"{prefix}.DBSubnetGroupArn", str(value["db_subnet_group_arn"])))
    if "supported_network_types" in value:
        import aws_sdk_neptune.types.string_list

        aws_sdk_neptune.types.string_list.serialize_query(
            value["supported_network_types"], pairs, f"{prefix}.SupportedNetworkTypes"
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
        import aws_sdk_neptune.types.subnet_list

        out["subnets"] = aws_sdk_neptune.types.subnet_list.deserialize_query(
            child_subnets
        )
    child_db_subnet_group_arn = el.find("DBSubnetGroupArn")
    if child_db_subnet_group_arn is not None:
        out["db_subnet_group_arn"] = str(child_db_subnet_group_arn.text or "")
    child_supported_network_types = el.find("SupportedNetworkTypes")
    if child_supported_network_types is not None:
        import aws_sdk_neptune.types.string_list

        out["supported_network_types"] = (
            aws_sdk_neptune.types.string_list.deserialize_query(
                child_supported_network_types
            )
        )
    return out
