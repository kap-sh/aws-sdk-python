"""Generated from Smithy shape ``com.amazonaws.ec2#SuccessfulInstanceCreditSpecificationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.successful_instance_credit_specification_item

SuccessfulInstanceCreditSpecificationSet: TypeAlias = list[
    "capo_ec2.types.successful_instance_credit_specification_item.SuccessfulInstanceCreditSpecificationItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SuccessfulInstanceCreditSpecificationSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.successful_instance_credit_specification_item

        capo_ec2.types.successful_instance_credit_specification_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SuccessfulInstanceCreditSpecificationSet:
    import capo_ec2.types.successful_instance_credit_specification_item

    out: SuccessfulInstanceCreditSpecificationSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.successful_instance_credit_specification_item.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> SuccessfulInstanceCreditSpecificationSet:
    import capo_ec2.types.successful_instance_credit_specification_item

    out: SuccessfulInstanceCreditSpecificationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.successful_instance_credit_specification_item.deserialize_ec2_query(
                child
            )
        )
    return out
