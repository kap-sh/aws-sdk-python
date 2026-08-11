"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStateChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_state_change

InstanceStateChangeList: TypeAlias = list[
    "capo_ec2.types.instance_state_change.InstanceStateChange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStateChangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_state_change

        capo_ec2.types.instance_state_change.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceStateChangeList:
    import capo_ec2.types.instance_state_change

    out: InstanceStateChangeList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_state_change.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceStateChangeList:
    import capo_ec2.types.instance_state_change

    out: InstanceStateChangeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_state_change.deserialize_ec2_query(child))
    return out
