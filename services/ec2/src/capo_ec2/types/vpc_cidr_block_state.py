"""Generated from Smithy shape ``com.amazonaws.ec2#VpcCidrBlockState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_cidr_block_state_code


class VpcCidrBlockState(TypedDict, closed=True):
    state: NotRequired["capo_ec2.types.vpc_cidr_block_state_code.VpcCidrBlockStateCode"]
    """<p>The state of the CIDR block.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message about the status of the CIDR block, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcCidrBlockState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_ec2.types.vpc_cidr_block_state_code

        capo_ec2.types.vpc_cidr_block_state_code.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))


def deserialize_ec2_query(el: Element) -> VpcCidrBlockState:
    out: VpcCidrBlockState = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.vpc_cidr_block_state_code

        out["state"] = capo_ec2.types.vpc_cidr_block_state_code.deserialize_ec2_query(
            child_state
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    return out
