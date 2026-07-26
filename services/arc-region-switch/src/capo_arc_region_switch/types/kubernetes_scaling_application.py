"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#KubernetesScalingApplication``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.regional_scaling_resource

KubernetesScalingApplication: TypeAlias = dict[
    "str",
    "capo_arc_region_switch.types.regional_scaling_resource.RegionalScalingResource",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: KubernetesScalingApplication) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_arc_region_switch.types.regional_scaling_resource

        out[key] = (
            capo_arc_region_switch.types.regional_scaling_resource.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KubernetesScalingApplication:
    out: KubernetesScalingApplication = {}
    for key, value in data.items():
        import capo_arc_region_switch.types.regional_scaling_resource

        out[key] = (
            capo_arc_region_switch.types.regional_scaling_resource.deserialize_aws_json_1_0(
                value
            )
        )
    return out
