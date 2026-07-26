"""Generated from Smithy shape ``com.amazonaws.ec2#UserIdGroupPairList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.user_id_group_pair

UserIdGroupPairList: TypeAlias = list[
    "capo_ec2.types.user_id_group_pair.UserIdGroupPair"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UserIdGroupPairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.user_id_group_pair

        capo_ec2.types.user_id_group_pair.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> UserIdGroupPairList:
    import capo_ec2.types.user_id_group_pair

    out: UserIdGroupPairList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.user_id_group_pair.deserialize_ec2_query(child))
    return out
