"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.listing_state


class InstanceCount(TypedDict):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of listed Reserved Instances in the state specified by the <code>state</code>.</p>"""
    state: NotRequired["aws_sdk_ec2.types.listing_state.ListingState"]
    """<p>The states of the listed Reserved Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceCount, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "state" in value:
        import aws_sdk_ec2.types.listing_state

        aws_sdk_ec2.types.listing_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> InstanceCount:
    out: InstanceCount = {}  # type: ignore[typeddict-item]
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.listing_state

        out["state"] = aws_sdk_ec2.types.listing_state.deserialize_ec2_query(
            child_state
        )
    return out
