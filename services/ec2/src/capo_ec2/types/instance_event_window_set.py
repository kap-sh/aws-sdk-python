"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_event_window

InstanceEventWindowSet: TypeAlias = list[
    "capo_ec2.types.instance_event_window.InstanceEventWindow"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_event_window

        capo_ec2.types.instance_event_window.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindowSet:
    import capo_ec2.types.instance_event_window

    out: InstanceEventWindowSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_event_window.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceEventWindowSet:
    import capo_ec2.types.instance_event_window

    out: InstanceEventWindowSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_event_window.deserialize_ec2_query(child))
    return out
