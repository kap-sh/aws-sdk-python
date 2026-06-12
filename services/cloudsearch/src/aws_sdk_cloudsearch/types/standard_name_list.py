"""Generated from Smithy shape ``com.amazonaws.cloudsearch#StandardNameList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.standard_name

StandardNameList: TypeAlias = list[
    "aws_sdk_cloudsearch.types.standard_name.StandardName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: StandardNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> StandardNameList:
    out: StandardNameList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: StandardNameList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> StandardNameList:
    out: StandardNameList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
