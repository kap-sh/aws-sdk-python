"""Generated from Smithy shape ``com.amazonaws.ecs#ResolvedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service_revision_load_balancers


class ResolvedConfiguration(TypedDict, closed=True):
    load_balancers: NotRequired[
        "capo_ecs.types.service_revision_load_balancers.ServiceRevisionLoadBalancers"
    ]
    """<p>The resolved load balancer configuration for the service revision. This includes information about which target groups serve traffic and which listener rules direct traffic to them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedConfiguration) -> dict:
    out: dict = {}
    if "load_balancers" in value:
        import capo_ecs.types.service_revision_load_balancers

        out["loadBalancers"] = (
            capo_ecs.types.service_revision_load_balancers.serialize_aws_json_1_1(
                value["load_balancers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedConfiguration:
    out: ResolvedConfiguration = {}  # type: ignore[typeddict-item]
    if "loadBalancers" in data:
        import capo_ecs.types.service_revision_load_balancers

        out["load_balancers"] = (
            capo_ecs.types.service_revision_load_balancers.deserialize_aws_json_1_1(
                data["loadBalancers"]
            )
        )
    return out
