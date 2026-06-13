"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VpcRouterNetworkInterfaceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.security_group_id_list


class VpcRouterNetworkInterfaceConfiguration(TypedDict):
    security_group_ids: (
        "aws_sdk_mediaconnect.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The IDs of the security groups to associate with the router network interface within the VPC.</p>"""
    subnet_id: "str"
    """<p>The ID of the subnet within the VPC to associate the router network interface with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcRouterNetworkInterfaceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.security_group_id_list

    out["securityGroupIds"] = (
        aws_sdk_mediaconnect.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    out["subnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> VpcRouterNetworkInterfaceConfiguration:
    out: VpcRouterNetworkInterfaceConfiguration = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import aws_sdk_mediaconnect.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_mediaconnect.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "VpcRouterNetworkInterfaceConfiguration.security_group_ids required"
        )
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    else:
        raise DeserializationError(
            "VpcRouterNetworkInterfaceConfiguration.subnet_id required"
        )
    return out
