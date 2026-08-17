"""Generated from Smithy shape ``com.amazonaws.ec2#UsageClassTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.usage_class_type

UsageClassTypeList: TypeAlias = list["capo_ec2.types.usage_class_type.UsageClassType"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UsageClassTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.usage_class_type

        capo_ec2.types.usage_class_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> UsageClassTypeList:
    import capo_ec2.types.usage_class_type

    out: UsageClassTypeList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.usage_class_type.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> UsageClassTypeList:
    import capo_ec2.types.usage_class_type

    out: UsageClassTypeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.usage_class_type.deserialize_ec2_query(child))
    return out
