"""Generated from Smithy shape ``com.amazonaws.ses#PolicyNameList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.policy_name

PolicyNameList: TypeAlias = list["aws_sdk_ses.types.policy_name.PolicyName"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> PolicyNameList:
    out: PolicyNameList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: PolicyNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> PolicyNameList:
    out: PolicyNameList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
