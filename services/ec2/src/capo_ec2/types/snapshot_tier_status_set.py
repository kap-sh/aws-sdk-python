"""Generated from Smithy shape ``com.amazonaws.ec2#snapshotTierStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.snapshot_tier_status

snapshotTierStatusSet: TypeAlias = list[
    "capo_ec2.types.snapshot_tier_status.SnapshotTierStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: snapshotTierStatusSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.snapshot_tier_status

        capo_ec2.types.snapshot_tier_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> snapshotTierStatusSet:
    import capo_ec2.types.snapshot_tier_status

    out: snapshotTierStatusSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.snapshot_tier_status.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> snapshotTierStatusSet:
    import capo_ec2.types.snapshot_tier_status

    out: snapshotTierStatusSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.snapshot_tier_status.deserialize_ec2_query(child))
    return out
