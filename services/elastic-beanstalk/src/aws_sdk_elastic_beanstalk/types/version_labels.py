"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#VersionLabels``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.version_label

VersionLabels: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.version_label.VersionLabel"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: VersionLabels, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> VersionLabels:
    out: VersionLabels = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: VersionLabels, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> VersionLabels:
    out: VersionLabels = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
