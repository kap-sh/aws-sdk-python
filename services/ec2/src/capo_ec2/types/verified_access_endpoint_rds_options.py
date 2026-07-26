"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointRdsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_endpoint_port_number
    import capo_ec2.types.verified_access_endpoint_protocol
    import capo_ec2.types.verified_access_endpoint_subnet_id_list


class VerifiedAccessEndpointRdsOptions(TypedDict, closed=True):
    protocol: NotRequired[
        "capo_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The protocol.</p>"""
    port: NotRequired[
        "capo_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The port.</p>"""
    rds_db_instance_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the RDS instance.</p>"""
    rds_db_cluster_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the DB cluster.</p>"""
    rds_db_proxy_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the RDS proxy.</p>"""
    rds_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The RDS endpoint.</p>"""
    subnet_ids: NotRequired[
        "capo_ec2.types.verified_access_endpoint_subnet_id_list.VerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessEndpointRdsOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "protocol" in value:
        import capo_ec2.types.verified_access_endpoint_protocol

        capo_ec2.types.verified_access_endpoint_protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "rds_db_instance_arn" in value:
        pairs.append((f"{prefix}.RdsDbInstanceArn", str(value["rds_db_instance_arn"])))
    if "rds_db_cluster_arn" in value:
        pairs.append((f"{prefix}.RdsDbClusterArn", str(value["rds_db_cluster_arn"])))
    if "rds_db_proxy_arn" in value:
        pairs.append((f"{prefix}.RdsDbProxyArn", str(value["rds_db_proxy_arn"])))
    if "rds_endpoint" in value:
        pairs.append((f"{prefix}.RdsEndpoint", str(value["rds_endpoint"])))
    if "subnet_ids" in value:
        import capo_ec2.types.verified_access_endpoint_subnet_id_list

        capo_ec2.types.verified_access_endpoint_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIdSet"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointRdsOptions:
    out: VerifiedAccessEndpointRdsOptions = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_ec2.types.verified_access_endpoint_protocol

        out["protocol"] = (
            capo_ec2.types.verified_access_endpoint_protocol.deserialize_ec2_query(
                child_protocol
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_rds_db_instance_arn = el.find("RdsDbInstanceArn")
    if child_rds_db_instance_arn is not None:
        out["rds_db_instance_arn"] = str(child_rds_db_instance_arn.text or "")
    child_rds_db_cluster_arn = el.find("RdsDbClusterArn")
    if child_rds_db_cluster_arn is not None:
        out["rds_db_cluster_arn"] = str(child_rds_db_cluster_arn.text or "")
    child_rds_db_proxy_arn = el.find("RdsDbProxyArn")
    if child_rds_db_proxy_arn is not None:
        out["rds_db_proxy_arn"] = str(child_rds_db_proxy_arn.text or "")
    child_rds_endpoint = el.find("RdsEndpoint")
    if child_rds_endpoint is not None:
        out["rds_endpoint"] = str(child_rds_endpoint.text or "")
    if el.find("SubnetIdSet") is not None:
        import capo_ec2.types.verified_access_endpoint_subnet_id_list

        out["subnet_ids"] = (
            capo_ec2.types.verified_access_endpoint_subnet_id_list.deserialize_ec2_query(
                el, "SubnetIdSet"
            )
        )
    return out
