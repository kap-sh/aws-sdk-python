"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import capo_route53_recovery_control_config.types.network_type


class UpdateClusterRequest(TypedDict, closed=True):
    cluster_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    network_type: NotRequired[
        "capo_route53_recovery_control_config.types.network_type.NetworkType"
    ]
    """<p>The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "network_type" in value:
        import capo_route53_recovery_control_config.types.network_type

        out["NetworkType"] = (
            capo_route53_recovery_control_config.types.network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "NetworkType" in data:
        import capo_route53_recovery_control_config.types.network_type

        out["network_type"] = (
            capo_route53_recovery_control_config.types.network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
