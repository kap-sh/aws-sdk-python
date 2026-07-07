"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.load_balancer_names_max20


class DescribeTagsInput(TypedDict, closed=True):
    load_balancer_names: "aws_sdk_elastic_load_balancing.types.load_balancer_names_max20.LoadBalancerNamesMax20"
    """<p>The names of the load balancers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing.types.load_balancer_names_max20

    aws_sdk_elastic_load_balancing.types.load_balancer_names_max20.serialize_query(
        value["load_balancer_names"], pairs, f"{prefix}.LoadBalancerNames"
    )


def deserialize_query(el: Element) -> DescribeTagsInput:
    out: DescribeTagsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_names = el.find("LoadBalancerNames")
    if child_load_balancer_names is not None:
        import aws_sdk_elastic_load_balancing.types.load_balancer_names_max20

        out["load_balancer_names"] = (
            aws_sdk_elastic_load_balancing.types.load_balancer_names_max20.deserialize_query(
                child_load_balancer_names
            )
        )
    else:
        raise DeserializationError("DescribeTagsInput.load_balancer_names required")
    return out
