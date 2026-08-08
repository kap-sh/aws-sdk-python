"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlExclusion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_encryption_control_exclusion_state


class VpcEncryptionControlExclusion(TypedDict, closed=True):
    state: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state.VpcEncryptionControlExclusionState"
    ]
    """<p>The current state of the exclusion configuration.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message providing additional information about the exclusion state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionControlExclusion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state

        capo_ec2.types.vpc_encryption_control_exclusion_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlExclusion:
    out: VpcEncryptionControlExclusion = {}  # type: ignore[typeddict-item]
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state

        out["state"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    return out
