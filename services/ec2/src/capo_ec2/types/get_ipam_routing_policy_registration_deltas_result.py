"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamRoutingPolicyRegistrationDeltasResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_routing_policy_registration_delta_set
    import capo_ec2.types.next_token


class GetIpamRoutingPolicyRegistrationDeltasResult(TypedDict, closed=True):
    ipam_routing_policy_registration_deltas: NotRequired[
        "capo_ec2.types.ipam_routing_policy_registration_delta_set.IpamRoutingPolicyRegistrationDeltaSet"
    ]
    """<p>The routing policy registration deltas.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamRoutingPolicyRegistrationDeltasResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_routing_policy_registration_deltas" in value:
        import capo_ec2.types.ipam_routing_policy_registration_delta_set

        capo_ec2.types.ipam_routing_policy_registration_delta_set.serialize_ec2_query(
            value["ipam_routing_policy_registration_deltas"],
            pairs,
            f"{key_prefix}IpamRoutingPolicyRegistrationDeltaSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamRoutingPolicyRegistrationDeltasResult:
    out: GetIpamRoutingPolicyRegistrationDeltasResult = {}  # type: ignore[typeddict-item]
    child_ipam_routing_policy_registration_deltas = el.find(
        "ipamRoutingPolicyRegistrationDeltaSet"
    )
    if child_ipam_routing_policy_registration_deltas is not None:
        import capo_ec2.types.ipam_routing_policy_registration_delta_set

        out["ipam_routing_policy_registration_deltas"] = (
            capo_ec2.types.ipam_routing_policy_registration_delta_set.deserialize_ec2_query(
                child_ipam_routing_policy_registration_deltas
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
