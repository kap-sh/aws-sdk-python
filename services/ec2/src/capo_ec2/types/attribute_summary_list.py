"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_summary

AttributeSummaryList: TypeAlias = list[
    "capo_ec2.types.attribute_summary.AttributeSummary"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttributeSummaryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.attribute_summary

        capo_ec2.types.attribute_summary.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AttributeSummaryList:
    import capo_ec2.types.attribute_summary

    out: AttributeSummaryList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.attribute_summary.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AttributeSummaryList:
    import capo_ec2.types.attribute_summary

    out: AttributeSummaryList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.attribute_summary.deserialize_ec2_query(child))
    return out
