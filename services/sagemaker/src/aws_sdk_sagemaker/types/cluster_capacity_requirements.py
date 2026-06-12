"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterCapacityRequirements``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_on_demand_options
    import aws_sdk_sagemaker.types.cluster_spot_options


class ClusterCapacityRequirements(TypedDict):
    spot: NotRequired["aws_sdk_sagemaker.types.cluster_spot_options.ClusterSpotOptions"]
    """<p>Configuration options specific to Spot instances.</p>"""
    on_demand: NotRequired[
        "aws_sdk_sagemaker.types.cluster_on_demand_options.ClusterOnDemandOptions"
    ]
    """<p>Configuration options specific to On-Demand instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterCapacityRequirements) -> dict:
    out: dict = {}
    if "spot" in value:
        import aws_sdk_sagemaker.types.cluster_spot_options

        out["Spot"] = (
            aws_sdk_sagemaker.types.cluster_spot_options.serialize_aws_json_1_1(
                value["spot"]
            )
        )
    if "on_demand" in value:
        import aws_sdk_sagemaker.types.cluster_on_demand_options

        out["OnDemand"] = (
            aws_sdk_sagemaker.types.cluster_on_demand_options.serialize_aws_json_1_1(
                value["on_demand"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterCapacityRequirements:
    out: ClusterCapacityRequirements = {}  # type: ignore[typeddict-item]
    if "Spot" in data:
        import aws_sdk_sagemaker.types.cluster_spot_options

        out["spot"] = (
            aws_sdk_sagemaker.types.cluster_spot_options.deserialize_aws_json_1_1(
                data["Spot"]
            )
        )
    if "OnDemand" in data:
        import aws_sdk_sagemaker.types.cluster_on_demand_options

        out["on_demand"] = (
            aws_sdk_sagemaker.types.cluster_on_demand_options.deserialize_aws_json_1_1(
                data["OnDemand"]
            )
        )
    return out
