"""Generated from Smithy shape ``com.amazonaws.wickr#WickrAwsNetworksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.wickr_aws_networks

WickrAwsNetworksList: TypeAlias = list[
    "capo_wickr.types.wickr_aws_networks.WickrAwsNetworks"
]


# --- restJson1 ser/de ---
def serialize_json(value: WickrAwsNetworksList) -> list:
    import capo_wickr.types.wickr_aws_networks

    out: list = []
    for item in value:
        out.append(capo_wickr.types.wickr_aws_networks.serialize_json(item))
    return out


def deserialize_json(data: list) -> WickrAwsNetworksList:
    import capo_wickr.types.wickr_aws_networks

    out: WickrAwsNetworksList = []
    for item in data:
        out.append(capo_wickr.types.wickr_aws_networks.deserialize_json(item))
    return out
