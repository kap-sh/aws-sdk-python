"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkCardInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_card_info

NetworkCardInfoList: TypeAlias = list[
    "capo_ec2.types.network_card_info.NetworkCardInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkCardInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.network_card_info

        capo_ec2.types.network_card_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> NetworkCardInfoList:
    import capo_ec2.types.network_card_info

    out: NetworkCardInfoList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.network_card_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> NetworkCardInfoList:
    import capo_ec2.types.network_card_info

    out: NetworkCardInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.network_card_info.deserialize_ec2_query(child))
    return out
