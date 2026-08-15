"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamRoutingPolicyRegistrationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_routing_policy_registration_delta


class DeleteIpamRoutingPolicyRegistrationResult(TypedDict, closed=True):
    ipam_routing_policy_registration_delta: NotRequired[
        "capo_ec2.types.ipam_routing_policy_registration_delta.IpamRoutingPolicyRegistrationDelta"
    ]
    """<p>Information about the routing policy registration delta created by this deletion.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamRoutingPolicyRegistrationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_routing_policy_registration_delta" in value:
        import capo_ec2.types.ipam_routing_policy_registration_delta

        capo_ec2.types.ipam_routing_policy_registration_delta.serialize_ec2_query(
            value["ipam_routing_policy_registration_delta"],
            pairs,
            f"{key_prefix}IpamRoutingPolicyRegistrationDelta",
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamRoutingPolicyRegistrationResult:
    out: DeleteIpamRoutingPolicyRegistrationResult = {}  # type: ignore[typeddict-item]
    child_ipam_routing_policy_registration_delta = el.find(
        "ipamRoutingPolicyRegistrationDelta"
    )
    if child_ipam_routing_policy_registration_delta is not None:
        import capo_ec2.types.ipam_routing_policy_registration_delta

        out["ipam_routing_policy_registration_delta"] = (
            capo_ec2.types.ipam_routing_policy_registration_delta.deserialize_ec2_query(
                child_ipam_routing_policy_registration_delta
            )
        )
    return out
