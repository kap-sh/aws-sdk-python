"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name

ApplicationNamesList: TypeAlias = list[
    "capo_elastic_beanstalk.types.application_name.ApplicationName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationNamesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> ApplicationNamesList:
    out: ApplicationNamesList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ApplicationNamesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ApplicationNamesList:
    out: ApplicationNamesList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
