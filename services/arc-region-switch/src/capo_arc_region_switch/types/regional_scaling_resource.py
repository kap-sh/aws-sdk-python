"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionalScalingResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.kubernetes_scaling_resource
    import capo_arc_region_switch.types.region

RegionalScalingResource: TypeAlias = dict[
    "capo_arc_region_switch.types.region.Region",
    "capo_arc_region_switch.types.kubernetes_scaling_resource.KubernetesScalingResource",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionalScalingResource) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.kubernetes_scaling_resource

        out[key] = (
            capo_arc_region_switch.types.kubernetes_scaling_resource.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionalScalingResource:
    out: RegionalScalingResource = {}
    for key, value in data.items():
        import capo_arc_region_switch.types.kubernetes_scaling_resource

        out[key] = (
            capo_arc_region_switch.types.kubernetes_scaling_resource.deserialize_aws_json_1_0(
                value
            )
        )
    return out
