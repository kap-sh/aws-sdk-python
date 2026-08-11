"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusEventList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_status_event

InstanceStatusEventList: TypeAlias = list[
    "capo_ec2.types.instance_status_event.InstanceStatusEvent"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStatusEventList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_status_event

        capo_ec2.types.instance_status_event.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceStatusEventList:
    import capo_ec2.types.instance_status_event

    out: InstanceStatusEventList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_status_event.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceStatusEventList:
    import capo_ec2.types.instance_status_event

    out: InstanceStatusEventList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_status_event.deserialize_ec2_query(child))
    return out
