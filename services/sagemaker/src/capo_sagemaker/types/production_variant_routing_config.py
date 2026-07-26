"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantRoutingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.routing_strategy


class ProductionVariantRoutingConfig(TypedDict, closed=True):
    routing_strategy: NotRequired[
        "capo_sagemaker.types.routing_strategy.RoutingStrategy"
    ]
    """<p>Sets how the endpoint routes incoming traffic:</p> <ul> <li> <p> <code>LEAST_OUTSTANDING_REQUESTS</code>: The endpoint routes requests to the specific instances that have more capacity to process them.</p> </li> <li> <p> <code>RANDOM</code>: The endpoint routes each request to a randomly chosen instance.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantRoutingConfig) -> dict:
    out: dict = {}
    if "routing_strategy" in value:
        import capo_sagemaker.types.routing_strategy

        out["RoutingStrategy"] = (
            capo_sagemaker.types.routing_strategy.serialize_aws_json_1_1(
                value["routing_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantRoutingConfig:
    out: ProductionVariantRoutingConfig = {}  # type: ignore[typeddict-item]
    if "RoutingStrategy" in data:
        import capo_sagemaker.types.routing_strategy

        out["routing_strategy"] = (
            capo_sagemaker.types.routing_strategy.deserialize_aws_json_1_1(
                data["RoutingStrategy"]
            )
        )
    return out
