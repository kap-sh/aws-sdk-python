"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointRdsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.modify_verified_access_endpoint_subnet_id_list
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_endpoint_port_number


class ModifyVerifiedAccessEndpointRdsOptions(TypedDict, closed=True):
    subnet_ids: NotRequired[
        "capo_ec2.types.modify_verified_access_endpoint_subnet_id_list.ModifyVerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
    port: NotRequired[
        "capo_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The port.</p>"""
    rds_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The RDS endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointRdsOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_ids" in value:
        import capo_ec2.types.modify_verified_access_endpoint_subnet_id_list

        capo_ec2.types.modify_verified_access_endpoint_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetId"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "rds_endpoint" in value:
        pairs.append((f"{key_prefix}RdsEndpoint", str(value["rds_endpoint"])))


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointRdsOptions:
    out: ModifyVerifiedAccessEndpointRdsOptions = {}  # type: ignore[typeddict-item]
    child_subnet_ids = el.find("SubnetId")
    if child_subnet_ids is not None:
        import capo_ec2.types.modify_verified_access_endpoint_subnet_id_list

        out["subnet_ids"] = (
            capo_ec2.types.modify_verified_access_endpoint_subnet_id_list.deserialize_ec2_query(
                child_subnet_ids
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_rds_endpoint = el.find("RdsEndpoint")
    if child_rds_endpoint is not None:
        out["rds_endpoint"] = str(child_rds_endpoint.text or "")
    return out
