"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerMonitoredTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_monitored_tag_key

CapacityManagerMonitoredTagKeyList: TypeAlias = list[
    "capo_ec2.types.capacity_manager_monitored_tag_key.CapacityManagerMonitoredTagKey"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerMonitoredTagKeyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_manager_monitored_tag_key

        capo_ec2.types.capacity_manager_monitored_tag_key.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityManagerMonitoredTagKeyList:
    import capo_ec2.types.capacity_manager_monitored_tag_key

    out: CapacityManagerMonitoredTagKeyList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_manager_monitored_tag_key.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityManagerMonitoredTagKeyList:
    import capo_ec2.types.capacity_manager_monitored_tag_key

    out: CapacityManagerMonitoredTagKeyList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_manager_monitored_tag_key.deserialize_ec2_query(
                child
            )
        )
    return out
