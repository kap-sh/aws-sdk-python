"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksResourceScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.eks_capacity_monitoring_approach
    import aws_sdk_arc_region_switch.types.eks_clusters
    import aws_sdk_arc_region_switch.types.eks_resource_scaling_ungraceful
    import aws_sdk_arc_region_switch.types.kubernetes_resource_type
    import aws_sdk_arc_region_switch.types.kubernetes_scaling_apps


class EksResourceScalingConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    kubernetes_resource_type: "aws_sdk_arc_region_switch.types.kubernetes_resource_type.KubernetesResourceType"
    """<p>The Kubernetes resource type for the configuration.</p>"""
    scaling_resources: NotRequired[
        "aws_sdk_arc_region_switch.types.kubernetes_scaling_apps.KubernetesScalingApps"
    ]
    """<p>The scaling resources for the configuration.</p>"""
    eks_clusters: NotRequired[
        "aws_sdk_arc_region_switch.types.eks_clusters.EksClusters"
    ]
    """<p>The clusters for the configuration.</p>"""
    ungraceful: NotRequired[
        "aws_sdk_arc_region_switch.types.eks_resource_scaling_ungraceful.EksResourceScalingUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""
    target_percent: "int"
    """<p>The target percentage for the configuration. The default is 100.</p>"""
    capacity_monitoring_approach: "aws_sdk_arc_region_switch.types.eks_capacity_monitoring_approach.EksCapacityMonitoringApproach"
    """<p>The monitoring approach for the configuration, that is, whether it was sampled in the last 24 hours or autoscaled in the last 24 hours.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EksResourceScalingConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import aws_sdk_arc_region_switch.types.kubernetes_resource_type

    out["kubernetesResourceType"] = (
        aws_sdk_arc_region_switch.types.kubernetes_resource_type.serialize_aws_json_1_0(
            value["kubernetes_resource_type"]
        )
    )
    if "scaling_resources" in value:
        import aws_sdk_arc_region_switch.types.kubernetes_scaling_apps

        out["scalingResources"] = (
            aws_sdk_arc_region_switch.types.kubernetes_scaling_apps.serialize_aws_json_1_0(
                value["scaling_resources"]
            )
        )
    if "eks_clusters" in value:
        import aws_sdk_arc_region_switch.types.eks_clusters

        out["eksClusters"] = (
            aws_sdk_arc_region_switch.types.eks_clusters.serialize_aws_json_1_0(
                value["eks_clusters"]
            )
        )
    if "ungraceful" in value:
        import aws_sdk_arc_region_switch.types.eks_resource_scaling_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.eks_resource_scaling_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["targetPercent"] = value.get("target_percent", 100)
    import aws_sdk_arc_region_switch.types.eks_capacity_monitoring_approach

    out["capacityMonitoringApproach"] = (
        aws_sdk_arc_region_switch.types.eks_capacity_monitoring_approach.serialize_aws_json_1_0(
            value.get("capacity_monitoring_approach", "sampledMaxInLast24Hours")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EksResourceScalingConfiguration:
    out: EksResourceScalingConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "kubernetesResourceType" in data:
        import aws_sdk_arc_region_switch.types.kubernetes_resource_type

        out["kubernetes_resource_type"] = (
            aws_sdk_arc_region_switch.types.kubernetes_resource_type.deserialize_aws_json_1_0(
                data["kubernetesResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "EksResourceScalingConfiguration.kubernetes_resource_type required"
        )
    if "scalingResources" in data:
        import aws_sdk_arc_region_switch.types.kubernetes_scaling_apps

        out["scaling_resources"] = (
            aws_sdk_arc_region_switch.types.kubernetes_scaling_apps.deserialize_aws_json_1_0(
                data["scalingResources"]
            )
        )
    if "eksClusters" in data:
        import aws_sdk_arc_region_switch.types.eks_clusters

        out["eks_clusters"] = (
            aws_sdk_arc_region_switch.types.eks_clusters.deserialize_aws_json_1_0(
                data["eksClusters"]
            )
        )
    if "ungraceful" in data:
        import aws_sdk_arc_region_switch.types.eks_resource_scaling_ungraceful

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.eks_resource_scaling_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if "targetPercent" in data:
        out["target_percent"] = data["targetPercent"]
    else:
        out["target_percent"] = 100
    if "capacityMonitoringApproach" in data:
        import aws_sdk_arc_region_switch.types.eks_capacity_monitoring_approach

        out["capacity_monitoring_approach"] = (
            aws_sdk_arc_region_switch.types.eks_capacity_monitoring_approach.deserialize_aws_json_1_0(
                data["capacityMonitoringApproach"]
            )
        )
    else:
        out["capacity_monitoring_approach"] = "sampledMaxInLast24Hours"
    return out
