"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.network_type


class CreateClusterRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>"""
    cluster_name: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the cluster.</p>"""
    tags: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
    ]
    """<p>The tags associated with the cluster.</p>"""
    network_type: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.network_type.NetworkType"
    ]
    """<p>The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "tags" in value:
        import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["Tags"] = (
            aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.serialize_json(
                value["tags"]
            )
        )
    if "network_type" in value:
        import aws_sdk_route53_recovery_control_config.types.network_type

        out["NetworkType"] = (
            aws_sdk_route53_recovery_control_config.types.network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "Tags" in data:
        import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["tags"] = (
            aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.deserialize_json(
                data["Tags"]
            )
        )
    if "NetworkType" in data:
        import aws_sdk_route53_recovery_control_config.types.network_type

        out["network_type"] = (
            aws_sdk_route53_recovery_control_config.types.network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
