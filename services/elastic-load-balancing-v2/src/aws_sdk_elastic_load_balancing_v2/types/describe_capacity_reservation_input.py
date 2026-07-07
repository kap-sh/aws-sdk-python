"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeCapacityReservationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn


class DescribeCapacityReservationInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeCapacityReservationInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))


def deserialize_query(el: Element) -> DescribeCapacityReservationInput:
    out: DescribeCapacityReservationInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    return out
