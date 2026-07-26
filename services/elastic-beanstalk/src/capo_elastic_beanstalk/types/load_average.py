"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#LoadAverage``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.load_average_value

LoadAverage: TypeAlias = list[
    "capo_elastic_beanstalk.types.load_average_value.LoadAverageValue"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadAverage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> LoadAverage:
    out: LoadAverage = []
    for child in el.findall("member"):
        out.append(float(child.text or ""))
    return out


def serialize_query_flat(
    value: LoadAverage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> LoadAverage:
    out: LoadAverage = []
    for child in parent.findall(tag):
        out.append(float(child.text or ""))
    return out
