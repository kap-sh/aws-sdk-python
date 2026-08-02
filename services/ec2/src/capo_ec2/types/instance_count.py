"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.listing_state


class InstanceCount(TypedDict, closed=True):
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of listed Reserved Instances in the state specified by the <code>state</code>.</p>"""
    state: NotRequired["capo_ec2.types.listing_state.ListingState"]
    """<p>The states of the listed Reserved Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceCount, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "state" in value:
        import capo_ec2.types.listing_state

        capo_ec2.types.listing_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> InstanceCount:
    out: InstanceCount = {}  # type: ignore[typeddict-item]
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.listing_state

        out["state"] = capo_ec2.types.listing_state.deserialize_ec2_query(child_state)
    return out
