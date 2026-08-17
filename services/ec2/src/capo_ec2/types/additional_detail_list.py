"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.additional_detail

AdditionalDetailList: TypeAlias = list[
    "capo_ec2.types.additional_detail.AdditionalDetail"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdditionalDetailList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.additional_detail

        capo_ec2.types.additional_detail.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AdditionalDetailList:
    import capo_ec2.types.additional_detail

    out: AdditionalDetailList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.additional_detail.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AdditionalDetailList:
    import capo_ec2.types.additional_detail

    out: AdditionalDetailList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.additional_detail.deserialize_ec2_query(child))
    return out
