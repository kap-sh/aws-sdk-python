"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ApplySecurityGroupsToLoadBalancerOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.security_groups


class ApplySecurityGroupsToLoadBalancerOutput(TypedDict):
    security_groups: NotRequired[
        "aws_sdk_elastic_load_balancing.types.security_groups.SecurityGroups"
    ]
    """<p>The IDs of the security groups associated with the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplySecurityGroupsToLoadBalancerOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "security_groups" in value:
        import aws_sdk_elastic_load_balancing.types.security_groups

        aws_sdk_elastic_load_balancing.types.security_groups.serialize_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroups"
        )


def deserialize_query(el: Element) -> ApplySecurityGroupsToLoadBalancerOutput:
    out: ApplySecurityGroupsToLoadBalancerOutput = {}  # type: ignore[typeddict-item]
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import aws_sdk_elastic_load_balancing.types.security_groups

        out["security_groups"] = (
            aws_sdk_elastic_load_balancing.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    return out
