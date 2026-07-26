"""Generated from Smithy shape ``com.amazonaws.cloudformation#LogicalResourceIds``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_id

LogicalResourceIds: TypeAlias = list[
    "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LogicalResourceIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> LogicalResourceIds:
    out: LogicalResourceIds = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: LogicalResourceIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> LogicalResourceIds:
    out: LogicalResourceIds = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
