"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#RegisterEndPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.instances


class RegisterEndPointsInput(TypedDict, closed=True):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    instances: "aws_sdk_elastic_load_balancing.types.instances.Instances"
    """<p>The IDs of the instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterEndPointsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    import aws_sdk_elastic_load_balancing.types.instances

    aws_sdk_elastic_load_balancing.types.instances.serialize_query(
        value["instances"], pairs, f"{prefix}.Instances"
    )


def deserialize_query(el: Element) -> RegisterEndPointsInput:
    out: RegisterEndPointsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError("RegisterEndPointsInput.load_balancer_name required")
    child_instances = el.find("Instances")
    if child_instances is not None:
        import aws_sdk_elastic_load_balancing.types.instances

        out["instances"] = (
            aws_sdk_elastic_load_balancing.types.instances.deserialize_query(
                child_instances
            )
        )
    else:
        raise DeserializationError("RegisterEndPointsInput.instances required")
    return out
