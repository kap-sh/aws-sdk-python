"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.snapshot

SnapshotList: TypeAlias = list["capo_ec2.types.snapshot.Snapshot"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.snapshot

        capo_ec2.types.snapshot.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> SnapshotList:
    import capo_ec2.types.snapshot

    out: SnapshotList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.snapshot.deserialize_ec2_query(child))
    return out
