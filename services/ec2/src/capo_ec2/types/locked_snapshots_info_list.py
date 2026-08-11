"""Generated from Smithy shape ``com.amazonaws.ec2#LockedSnapshotsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.locked_snapshots_info

LockedSnapshotsInfoList: TypeAlias = list[
    "capo_ec2.types.locked_snapshots_info.LockedSnapshotsInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LockedSnapshotsInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.locked_snapshots_info

        capo_ec2.types.locked_snapshots_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LockedSnapshotsInfoList:
    import capo_ec2.types.locked_snapshots_info

    out: LockedSnapshotsInfoList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.locked_snapshots_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LockedSnapshotsInfoList:
    import capo_ec2.types.locked_snapshots_info

    out: LockedSnapshotsInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.locked_snapshots_info.deserialize_ec2_query(child))
    return out
