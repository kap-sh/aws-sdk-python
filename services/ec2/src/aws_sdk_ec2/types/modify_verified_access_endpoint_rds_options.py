"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointRdsOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_port_number


class ModifyVerifiedAccessEndpointRdsOptions(TypedDict):
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list.ModifyVerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The port.</p>"""
    rds_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The RDS endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointRdsOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "subnet_ids" in value:
        import aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list

        aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "rds_endpoint" in value:
        pairs.append((f"{prefix}.RdsEndpoint", str(value["rds_endpoint"])))


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointRdsOptions:
    out: ModifyVerifiedAccessEndpointRdsOptions = {}  # type: ignore[typeddict-item]
    if el.find("SubnetIds") is not None:
        import aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list.deserialize_ec2_query(
                el, "SubnetIds"
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_rds_endpoint = el.find("RdsEndpoint")
    if child_rds_endpoint is not None:
        out["rds_endpoint"] = str(child_rds_endpoint.text or "")
    return out
