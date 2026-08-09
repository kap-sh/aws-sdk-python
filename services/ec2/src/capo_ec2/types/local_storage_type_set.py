"""Generated from Smithy shape ``com.amazonaws.ec2#LocalStorageTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_storage_type

LocalStorageTypeSet: TypeAlias = list[
    "capo_ec2.types.local_storage_type.LocalStorageType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalStorageTypeSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.local_storage_type

        capo_ec2.types.local_storage_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LocalStorageTypeSet:
    import capo_ec2.types.local_storage_type

    out: LocalStorageTypeSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.local_storage_type.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LocalStorageTypeSet:
    import capo_ec2.types.local_storage_type

    out: LocalStorageTypeSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.local_storage_type.deserialize_ec2_query(child))
    return out
