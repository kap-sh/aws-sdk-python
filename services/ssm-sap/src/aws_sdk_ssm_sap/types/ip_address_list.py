"""Generated from Smithy shape ``com.amazonaws.ssmsap#IpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.ip_address_member

IpAddressList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.ip_address_member.IpAddressMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressList) -> list:
    import aws_sdk_ssm_sap.types.ip_address_member

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.ip_address_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> IpAddressList:
    import aws_sdk_ssm_sap.types.ip_address_member

    out: IpAddressList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.ip_address_member.deserialize_json(item))
    return out
