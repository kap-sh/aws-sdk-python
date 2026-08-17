"""Generated from Smithy shape ``com.amazonaws.ec2#UserIdGroupPairSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.user_id_group_pair

UserIdGroupPairSet: TypeAlias = list[
    "capo_ec2.types.user_id_group_pair.UserIdGroupPair"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UserIdGroupPairSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.user_id_group_pair

        capo_ec2.types.user_id_group_pair.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> UserIdGroupPairSet:
    import capo_ec2.types.user_id_group_pair

    out: UserIdGroupPairSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.user_id_group_pair.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> UserIdGroupPairSet:
    import capo_ec2.types.user_id_group_pair

    out: UserIdGroupPairSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.user_id_group_pair.deserialize_ec2_query(child))
    return out
