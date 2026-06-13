"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#VpcInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.ip_address_type
    import aws_sdk_pca_connector_ad.types.security_group_id_list


class VpcInformation(TypedDict):
    ip_address_type: NotRequired[
        "aws_sdk_pca_connector_ad.types.ip_address_type.IpAddressType"
    ]
    """<p>The VPC IP address type.</p>"""
    security_group_ids: (
        "aws_sdk_pca_connector_ad.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The security groups used with the connector. You can use a maximum of 4 security groups with a connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInformation) -> dict:
    out: dict = {}
    if "ip_address_type" in value:
        import aws_sdk_pca_connector_ad.types.ip_address_type

        out["IpAddressType"] = (
            aws_sdk_pca_connector_ad.types.ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    import aws_sdk_pca_connector_ad.types.security_group_id_list

    out["SecurityGroupIds"] = (
        aws_sdk_pca_connector_ad.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> VpcInformation:
    out: VpcInformation = {}  # type: ignore[typeddict-item]
    if "IpAddressType" in data:
        import aws_sdk_pca_connector_ad.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_pca_connector_ad.types.ip_address_type.deserialize_json(
                data["IpAddressType"]
            )
        )
    if "SecurityGroupIds" in data:
        import aws_sdk_pca_connector_ad.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_pca_connector_ad.types.security_group_id_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcInformation.security_group_ids required")
    return out
