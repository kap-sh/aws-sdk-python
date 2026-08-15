"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRoutingPolicyRegistrationDelta``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_routing_policy_registration_delta_state
    import capo_ec2.types.string


class IpamRoutingPolicyRegistrationDelta(TypedDict, closed=True):
    delta_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The unique identifier of the delta.</p>"""
    delta_json: NotRequired["capo_ec2.types.string.String"]
    """<p>The JSON specification describing the changes applied in this delta.</p>"""
    state: NotRequired[
        "capo_ec2.types.ipam_routing_policy_registration_delta_state.IpamRoutingPolicyRegistrationDeltaState"
    ]
    """<p>The state of the delta. Valid values: <code>pending</code> | <code>published</code> | <code>failed</code>.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message describing the current state, including error information if the delta failed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamRoutingPolicyRegistrationDelta, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "delta_id" in value:
        pairs.append((f"{key_prefix}DeltaId", str(value["delta_id"])))
    if "delta_json" in value:
        pairs.append((f"{key_prefix}DeltaJson", str(value["delta_json"])))
    if "state" in value:
        import capo_ec2.types.ipam_routing_policy_registration_delta_state

        capo_ec2.types.ipam_routing_policy_registration_delta_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))


def deserialize_ec2_query(el: Element) -> IpamRoutingPolicyRegistrationDelta:
    out: IpamRoutingPolicyRegistrationDelta = {}  # type: ignore[typeddict-item]
    child_delta_id = el.find("deltaId")
    if child_delta_id is not None:
        out["delta_id"] = str(child_delta_id.text or "")
    child_delta_json = el.find("deltaJson")
    if child_delta_json is not None:
        out["delta_json"] = str(child_delta_json.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_routing_policy_registration_delta_state

        out["state"] = (
            capo_ec2.types.ipam_routing_policy_registration_delta_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    return out
