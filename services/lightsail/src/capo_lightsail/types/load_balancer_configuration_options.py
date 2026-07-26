"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerConfigurationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_attribute_name
    import capo_lightsail.types.string

LoadBalancerConfigurationOptions: TypeAlias = dict[
    "capo_lightsail.types.load_balancer_attribute_name.LoadBalancerAttributeName",
    "capo_lightsail.types.string.string",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: LoadBalancerConfigurationOptions,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lightsail.types.load_balancer_attribute_name

        out[
            capo_lightsail.types.load_balancer_attribute_name.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancerConfigurationOptions:
    out: LoadBalancerConfigurationOptions = {}
    for key, value in data.items():
        import capo_lightsail.types.load_balancer_attribute_name

        out[
            capo_lightsail.types.load_balancer_attribute_name.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out
