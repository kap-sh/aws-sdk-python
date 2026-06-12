"""Generated from Smithy shape ``com.amazonaws.wickr#WickrAwsNetworksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.wickr_aws_networks

WickrAwsNetworksList: TypeAlias = list[
    "aws_sdk_wickr.types.wickr_aws_networks.WickrAwsNetworks"
]


# --- restJson1 ser/de ---
def serialize_json(value: WickrAwsNetworksList) -> list:
    import aws_sdk_wickr.types.wickr_aws_networks

    out: list = []
    for item in value:
        out.append(aws_sdk_wickr.types.wickr_aws_networks.serialize_json(item))
    return out


def deserialize_json(data: list) -> WickrAwsNetworksList:
    import aws_sdk_wickr.types.wickr_aws_networks

    out: WickrAwsNetworksList = []
    for item in data:
        out.append(aws_sdk_wickr.types.wickr_aws_networks.deserialize_json(item))
    return out
