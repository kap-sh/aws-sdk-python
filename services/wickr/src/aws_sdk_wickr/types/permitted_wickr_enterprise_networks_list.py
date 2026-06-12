"""Generated from Smithy shape ``com.amazonaws.wickr#PermittedWickrEnterpriseNetworksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.permitted_wickr_enterprise_network

PermittedWickrEnterpriseNetworksList: TypeAlias = list[
    "aws_sdk_wickr.types.permitted_wickr_enterprise_network.PermittedWickrEnterpriseNetwork"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermittedWickrEnterpriseNetworksList) -> list:
    import aws_sdk_wickr.types.permitted_wickr_enterprise_network

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wickr.types.permitted_wickr_enterprise_network.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PermittedWickrEnterpriseNetworksList:
    import aws_sdk_wickr.types.permitted_wickr_enterprise_network

    out: PermittedWickrEnterpriseNetworksList = []
    for item in data:
        out.append(
            aws_sdk_wickr.types.permitted_wickr_enterprise_network.deserialize_json(
                item
            )
        )
    return out
