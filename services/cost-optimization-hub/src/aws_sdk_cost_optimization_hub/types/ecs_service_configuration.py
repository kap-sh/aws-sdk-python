"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EcsServiceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.compute_configuration


class EcsServiceConfiguration(TypedDict):
    compute: NotRequired[
        "aws_sdk_cost_optimization_hub.types.compute_configuration.ComputeConfiguration"
    ]
    """<p>Details about the compute configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EcsServiceConfiguration) -> dict:
    out: dict = {}
    if "compute" in value:
        import aws_sdk_cost_optimization_hub.types.compute_configuration

        out["compute"] = (
            aws_sdk_cost_optimization_hub.types.compute_configuration.serialize_aws_json_1_0(
                value["compute"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EcsServiceConfiguration:
    out: EcsServiceConfiguration = {}  # type: ignore[typeddict-item]
    if "compute" in data:
        import aws_sdk_cost_optimization_hub.types.compute_configuration

        out["compute"] = (
            aws_sdk_cost_optimization_hub.types.compute_configuration.deserialize_aws_json_1_0(
                data["compute"]
            )
        )
    return out
