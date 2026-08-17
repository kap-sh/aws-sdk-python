"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.delete_fleet_error_item

DeleteFleetErrorSet: TypeAlias = list[
    "capo_ec2.types.delete_fleet_error_item.DeleteFleetErrorItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFleetErrorSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.delete_fleet_error_item

        capo_ec2.types.delete_fleet_error_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> DeleteFleetErrorSet:
    import capo_ec2.types.delete_fleet_error_item

    out: DeleteFleetErrorSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.delete_fleet_error_item.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DeleteFleetErrorSet:
    import capo_ec2.types.delete_fleet_error_item

    out: DeleteFleetErrorSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.delete_fleet_error_item.deserialize_ec2_query(child))
    return out
