"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceRefreshIds``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255

InstanceRefreshIds: TypeAlias = list[
    "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceRefreshIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> InstanceRefreshIds:
    out: InstanceRefreshIds = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: InstanceRefreshIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> InstanceRefreshIds:
    out: InstanceRefreshIds = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
