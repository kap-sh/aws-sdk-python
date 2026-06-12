"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Causes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.cause

Causes: TypeAlias = list["aws_sdk_elastic_beanstalk.types.cause.Cause"]


# --- awsQuery ser/de ---
def serialize_query(value: Causes, pairs: list[tuple[str, str]], prefix: str) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> Causes:
    out: Causes = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: Causes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> Causes:
    out: Causes = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
