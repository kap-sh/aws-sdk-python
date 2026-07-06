"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#RegisterEndPointsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.instances


class RegisterEndPointsOutput(TypedDict, closed=True):
    instances: NotRequired["aws_sdk_elastic_load_balancing.types.instances.Instances"]
    """<p>The updated list of instances for the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterEndPointsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instances" in value:
        import aws_sdk_elastic_load_balancing.types.instances

        aws_sdk_elastic_load_balancing.types.instances.serialize_query(
            value["instances"], pairs, f"{prefix}.Instances"
        )


def deserialize_query(el: Element) -> RegisterEndPointsOutput:
    out: RegisterEndPointsOutput = {}  # type: ignore[typeddict-item]
    child_instances = el.find("Instances")
    if child_instances is not None:
        import aws_sdk_elastic_load_balancing.types.instances

        out["instances"] = (
            aws_sdk_elastic_load_balancing.types.instances.deserialize_query(
                child_instances
            )
        )
    return out
