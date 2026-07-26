"""Generated from Smithy shape ``com.amazonaws.datazone#NetworkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.network_access_type
    import capo_datazone.types.security_group_ids
    import capo_datazone.types.subnet_ids


class NetworkConfig(TypedDict, closed=True):
    network_access_type: "capo_datazone.types.network_access_type.NetworkAccessType"
    """<p>The network access type for the notebook run. Valid values are <code>PUBLIC_INTERNET_ONLY</code> and <code>VPC_ONLY</code>.</p>"""
    vpc_id: NotRequired["str"]
    """<p>The identifier of the VPC for the notebook run. This is required when the network access type is <code>VPC_ONLY</code>.</p>"""
    subnet_ids: NotRequired["capo_datazone.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets for the notebook run. You can specify up to 10 subnets.</p>"""
    security_group_ids: NotRequired[
        "capo_datazone.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The identifiers of the security groups for the notebook run. You can specify up to 5 security groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfig) -> dict:
    out: dict = {}
    import capo_datazone.types.network_access_type

    out["networkAccessType"] = capo_datazone.types.network_access_type.serialize_json(
        value["network_access_type"]
    )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_datazone.types.subnet_ids

        out["subnetIds"] = capo_datazone.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_datazone.types.security_group_ids

        out["securityGroupIds"] = capo_datazone.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    return out


def deserialize_json(data: dict) -> NetworkConfig:
    out: NetworkConfig = {}  # type: ignore[typeddict-item]
    if "networkAccessType" in data:
        import capo_datazone.types.network_access_type

        out["network_access_type"] = (
            capo_datazone.types.network_access_type.deserialize_json(
                data["networkAccessType"]
            )
        )
    else:
        raise DeserializationError("NetworkConfig.network_access_type required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "subnetIds" in data:
        import capo_datazone.types.subnet_ids

        out["subnet_ids"] = capo_datazone.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import capo_datazone.types.security_group_ids

        out["security_group_ids"] = (
            capo_datazone.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
