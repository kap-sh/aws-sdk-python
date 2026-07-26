"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DeregisterEndPointsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.instances


class DeregisterEndPointsOutput(TypedDict, closed=True):
    instances: NotRequired["capo_elastic_load_balancing.types.instances.Instances"]
    """<p>The remaining instances registered with the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterEndPointsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instances" in value:
        import capo_elastic_load_balancing.types.instances

        capo_elastic_load_balancing.types.instances.serialize_query(
            value["instances"], pairs, f"{prefix}.Instances"
        )


def deserialize_query(el: Element) -> DeregisterEndPointsOutput:
    out: DeregisterEndPointsOutput = {}  # type: ignore[typeddict-item]
    child_instances = el.find("Instances")
    if child_instances is not None:
        import capo_elastic_load_balancing.types.instances

        out["instances"] = (
            capo_elastic_load_balancing.types.instances.deserialize_query(
                child_instances
            )
        )
    return out
