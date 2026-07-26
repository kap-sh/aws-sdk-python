"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2InstanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.instance_configuration


class Ec2InstanceConfiguration(TypedDict, closed=True):
    instance: NotRequired[
        "capo_cost_optimization_hub.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>Details about the instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2InstanceConfiguration) -> dict:
    out: dict = {}
    if "instance" in value:
        import capo_cost_optimization_hub.types.instance_configuration

        out["instance"] = (
            capo_cost_optimization_hub.types.instance_configuration.serialize_aws_json_1_0(
                value["instance"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2InstanceConfiguration:
    out: Ec2InstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import capo_cost_optimization_hub.types.instance_configuration

        out["instance"] = (
            capo_cost_optimization_hub.types.instance_configuration.deserialize_aws_json_1_0(
                data["instance"]
            )
        )
    return out
