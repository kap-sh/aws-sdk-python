"""Generated from Smithy shape ``com.amazonaws.ec2#ConditionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.condition_value

ConditionValueList: TypeAlias = list["capo_ec2.types.condition_value.ConditionValue"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConditionValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> ConditionValueList:
    out: ConditionValueList = []
    for child in el.findall("item"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ConditionValueList:
    out: ConditionValueList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
