"""Generated from Smithy shape ``com.amazonaws.kafka#Serverless``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_vpc_config
    import capo_kafka.types.serverless_client_authentication
    import capo_kafka.types.serverless_connectivity_info


class Serverless(TypedDict, closed=True):
    vpc_configs: NotRequired["capo_kafka.types.__list_of_vpc_config.__listOfVpcConfig"]
    """<p>The configuration of the Amazon VPCs for the cluster.</p>"""
    client_authentication: NotRequired[
        "capo_kafka.types.serverless_client_authentication.ServerlessClientAuthentication"
    ]
    """<p>Includes all client authentication information.</p>"""
    connectivity_info: NotRequired[
        "capo_kafka.types.serverless_connectivity_info.ServerlessConnectivityInfo"
    ]
    """<p>Describes the cluster's connectivity information, such as its network type, which is IPv4 or DUAL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Serverless) -> dict:
    out: dict = {}
    if "vpc_configs" in value:
        import capo_kafka.types.__list_of_vpc_config

        out["vpcConfigs"] = capo_kafka.types.__list_of_vpc_config.serialize_json(
            value["vpc_configs"]
        )
    if "client_authentication" in value:
        import capo_kafka.types.serverless_client_authentication

        out["clientAuthentication"] = (
            capo_kafka.types.serverless_client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "connectivity_info" in value:
        import capo_kafka.types.serverless_connectivity_info

        out["connectivityInfo"] = (
            capo_kafka.types.serverless_connectivity_info.serialize_json(
                value["connectivity_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> Serverless:
    out: Serverless = {}  # type: ignore[typeddict-item]
    if "vpcConfigs" in data:
        import capo_kafka.types.__list_of_vpc_config

        out["vpc_configs"] = capo_kafka.types.__list_of_vpc_config.deserialize_json(
            data["vpcConfigs"]
        )
    if "clientAuthentication" in data:
        import capo_kafka.types.serverless_client_authentication

        out["client_authentication"] = (
            capo_kafka.types.serverless_client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    if "connectivityInfo" in data:
        import capo_kafka.types.serverless_connectivity_info

        out["connectivity_info"] = (
            capo_kafka.types.serverless_connectivity_info.deserialize_json(
                data["connectivityInfo"]
            )
        )
    return out
